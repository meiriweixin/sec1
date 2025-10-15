import { useState, useEffect } from "react";
import { motion, useAnimation } from "framer-motion";
import { Button } from "@/components/ui/button";
import { Slider } from "@/components/ui/slider";
import { Play, Pause, RotateCcw } from "lucide-react";

interface ForceMotionProps {
  showVectors?: boolean;
  showGraph?: boolean;
}

export function ForceMotion({ showVectors = true, showGraph = true }: ForceMotionProps) {
  const controls = useAnimation();
  const [isPlaying, setIsPlaying] = useState(false);
  const [mass, setMass] = useState(5); // kg
  const [force, setForce] = useState(10); // N
  const [friction, setFriction] = useState(2); // N
  const [position, setPosition] = useState(0);
  const [velocity, setVelocity] = useState(0);
  const [time, setTime] = useState(0);

  // Calculate net force considering friction behavior
  // Friction only acts when there's motion or when applied force overcomes static friction
  let netForce: number;
  let acceleration: number;

  if (velocity === 0) {
    // Object at rest: static friction can equal applied force up to a limit
    if (Math.abs(force) <= friction) {
      // Applied force doesn't overcome static friction
      netForce = 0;
      acceleration = 0;
    } else {
      // Applied force overcomes static friction
      netForce = force - friction;
      acceleration = netForce / mass;
    }
  } else {
    // Object in motion: kinetic friction opposes motion
    const frictionForce = velocity > 0 ? friction : -friction;
    netForce = force - frictionForce;
    acceleration = netForce / mass;
  }

  useEffect(() => {
    if (isPlaying) {
      const interval = setInterval(() => {
        setTime(t => t + 0.1);
        setVelocity(v => {
          const newVelocity = v + acceleration * 0.1;

          // If velocity would change direction due to friction, stop instead
          if (v > 0 && newVelocity < 0 && force === 0) {
            return 0;
          }
          if (v < 0 && newVelocity > 0 && force === 0) {
            return 0;
          }

          return newVelocity;
        });
        setPosition(p => {
          const newPos = p + velocity * 0.1;
          // Stop at the edge
          if (newPos >= 300) {
            setIsPlaying(false);
            return 300;
          }
          // Don't allow negative position
          if (newPos < 0) {
            setIsPlaying(false);
            return 0;
          }
          return newPos;
        });
      }, 50);
      return () => clearInterval(interval);
    }
  }, [isPlaying, velocity, acceleration, force]);

  const handleReset = () => {
    setIsPlaying(false);
    setPosition(0);
    setVelocity(0);
    setTime(0);
  };

  const handlePlayPause = () => {
    setIsPlaying(!isPlaying);
  };

  return (
    <div className="w-full max-w-4xl mx-auto p-8 bg-lesson-bg rounded-lg">
      <div className="text-center mb-6">
        <h3 className="text-lg font-semibold text-foreground">Force and Motion</h3>
        <p className="text-sm text-muted-foreground">
          Explore Newton's Second Law: F = ma
        </p>
      </div>

      {/* Animation Area */}
      <div className="bg-gradient-to-b from-sky-100 to-gray-100 dark:from-sky-900/20 dark:to-gray-900/20 rounded-lg p-6 mb-6">
        <div className="relative h-32 mb-4">
          {/* Ground */}
          <div className="absolute bottom-0 w-full h-1 bg-gray-500"></div>
          
          {/* Distance markers */}
          <div className="absolute bottom-2 w-full flex justify-between text-xs text-muted-foreground">
            <span>0m</span>
            <span>100m</span>
            <span>200m</span>
            <span>300m</span>
          </div>

          {/* Object */}
          <motion.div
            className="absolute bottom-1"
            animate={{ x: position }}
            transition={{ type: "tween", ease: "linear" }}
            style={{ left: 50 }}
          >
            <div 
              className="relative bg-primary rounded w-12 h-12 flex items-center justify-center text-primary-foreground font-bold"
              style={{ transform: `scale(${0.5 + mass * 0.1})` }}
            >
              {mass}kg
            </div>
            
            {/* Force Vectors */}
            {showVectors && (
              <>
                {/* Applied Force Arrow */}
                <svg
                  className="absolute top-1/2 -translate-y-1/2"
                  style={{ left: '100%' }}
                  width={force * 3}
                  height="20"
                >
                  <defs>
                    <marker
                      id="arrowhead-force"
                      markerWidth="10"
                      markerHeight="7"
                      refX="9"
                      refY="3.5"
                      orient="auto"
                    >
                      <polygon
                        points="0 0, 10 3.5, 0 7"
                        fill="rgb(34, 197, 94)"
                      />
                    </marker>
                  </defs>
                  <line
                    x1="0"
                    y1="10"
                    x2={force * 3 - 5}
                    y2="10"
                    stroke="rgb(34, 197, 94)"
                    strokeWidth="3"
                    markerEnd="url(#arrowhead-force)"
                  />
                  <text x={force * 1.5} y="7" className="text-xs fill-green-600 font-medium">
                    {force}N
                  </text>
                </svg>

                {/* Friction Force Arrow */}
                {friction > 0 && velocity > 0 && (
                  <svg
                    className="absolute top-1/2 -translate-y-1/2"
                    style={{ right: '100%' }}
                    width={friction * 3}
                    height="20"
                  >
                    <defs>
                      <marker
                        id="arrowhead-friction"
                        markerWidth="10"
                        markerHeight="7"
                        refX="1"
                        refY="3.5"
                        orient="auto"
                      >
                        <polygon
                          points="10 0, 0 3.5, 10 7"
                          fill="rgb(239, 68, 68)"
                        />
                      </marker>
                    </defs>
                    <line
                      x1={friction * 3}
                      y1="10"
                      x2="5"
                      y2="10"
                      stroke="rgb(239, 68, 68)"
                      strokeWidth="3"
                      markerEnd="url(#arrowhead-friction)"
                    />
                    <text x={friction * 1.5} y="7" className="text-xs fill-red-600 font-medium">
                      {friction}N
                    </text>
                  </svg>
                )}
              </>
            )}
          </motion.div>
        </div>

        {/* Info Display */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm">
          <div className="bg-card p-2 rounded text-center">
            <div className="text-muted-foreground text-xs">Net Force</div>
            <div className="font-mono font-bold text-primary">{netForce.toFixed(1)} N</div>
          </div>
          <div className="bg-card p-2 rounded text-center">
            <div className="text-muted-foreground text-xs">Acceleration</div>
            <div className="font-mono font-bold text-accent">{acceleration.toFixed(2)} m/s²</div>
          </div>
          <div className="bg-card p-2 rounded text-center">
            <div className="text-muted-foreground text-xs">Velocity</div>
            <div className="font-mono font-bold text-warning">{velocity.toFixed(1)} m/s</div>
          </div>
          <div className="bg-card p-2 rounded text-center">
            <div className="text-muted-foreground text-xs">Time</div>
            <div className="font-mono font-bold">{time.toFixed(1)} s</div>
          </div>
        </div>
      </div>

      {/* Controls */}
      <div className="space-y-4 mb-6">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div>
            <label className="text-sm font-medium">Mass: {mass} kg</label>
            <Slider
              value={[mass]}
              onValueChange={(value) => setMass(value[0])}
              max={20}
              min={1}
              step={1}
              className="mt-2"
              disabled={isPlaying}
            />
          </div>
          <div>
            <label className="text-sm font-medium">Applied Force: {force} N</label>
            <Slider
              value={[force]}
              onValueChange={(value) => setForce(value[0])}
              max={50}
              min={0}
              step={1}
              className="mt-2"
              disabled={isPlaying}
            />
          </div>
          <div>
            <label className="text-sm font-medium">Friction: {friction} N</label>
            <Slider
              value={[friction]}
              onValueChange={(value) => setFriction(value[0])}
              max={20}
              min={0}
              step={1}
              className="mt-2"
              disabled={isPlaying}
            />
          </div>
        </div>

        <div className="flex justify-center space-x-2">
          <Button
            onClick={handlePlayPause}
            className="btn-primary"
            disabled={position >= 300}
          >
            {isPlaying ? (
              <>
                <Pause className="mr-2 h-4 w-4" /> Pause
              </>
            ) : (
              <>
                <Play className="mr-2 h-4 w-4" /> Start
              </>
            )}
          </Button>
          <Button onClick={handleReset} variant="outline">
            <RotateCcw className="mr-2 h-4 w-4" /> Reset
          </Button>
        </div>
      </div>

      {/* Equations */}
      <div className="bg-muted/50 p-4 rounded-lg space-y-2 text-sm">
        <div className="font-mono text-center space-y-1">
          <div>F_net = F_applied - F_friction = {force} - {friction} = {netForce} N</div>
          <div>a = F_net / m = {netForce} / {mass} = {acceleration.toFixed(2)} m/s²</div>
          <div>v = v₀ + at = 0 + {acceleration.toFixed(2)} × {time.toFixed(1)} = {velocity.toFixed(1)} m/s</div>
        </div>
      </div>

      {/* Key Concepts */}
      <div className="mt-6 p-4 bg-gradient-to-r from-primary-soft/50 to-accent-soft/50 rounded-lg">
        <h4 className="font-medium mb-2">Key Concepts:</h4>
        <ul className="text-sm space-y-1 text-muted-foreground">
          <li>• Greater force produces greater acceleration</li>
          <li>• Greater mass requires more force for the same acceleration</li>
          <li>• Friction opposes motion and reduces net force</li>
          <li>• When forces are balanced (F_net = 0), there is no acceleration</li>
        </ul>
      </div>
    </div>
  );
}












