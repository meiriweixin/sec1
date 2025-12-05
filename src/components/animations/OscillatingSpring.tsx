import { useState, useEffect } from 'react';
import { Play, Pause, RotateCcw } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Slider } from '@/components/ui/slider';

interface OscillatingSpringProps {
  amplitude?: number;
  frequency?: number;
  mass?: number;
}

export default function OscillatingSpring({
  amplitude = 50,
  frequency = 1,
  mass = 1
}: OscillatingSpringProps) {
  const [time, setTime] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [userAmplitude, setUserAmplitude] = useState(amplitude);
  const [userFrequency, setUserFrequency] = useState(frequency);

  useEffect(() => {
    if (!isPlaying) return;

    const interval = setInterval(() => {
      setTime(t => t + 0.05);
    }, 50);

    return () => clearInterval(interval);
  }, [isPlaying]);

  // Calculate position using SHM equation: x = A * cos(ωt)
  const omega = 2 * Math.PI * userFrequency;
  const displacement = userAmplitude * Math.cos(omega * time);
  const velocity = -userAmplitude * omega * Math.sin(omega * time);
  const acceleration = -userAmplitude * omega * omega * Math.cos(omega * time);

  // Calculate energies
  const k = mass * omega * omega; // Spring constant
  const kineticEnergy = 0.5 * mass * velocity * velocity;
  const potentialEnergy = 0.5 * k * displacement * displacement;
  const totalEnergy = kineticEnergy + potentialEnergy;

  const handleReset = () => {
    setTime(0);
    setIsPlaying(false);
  };

  return (
    <div className="w-full max-w-4xl mx-auto p-6 bg-gradient-to-br from-blue-50 to-purple-50 dark:from-gray-800 dark:to-gray-900 rounded-lg">
      <h3 className="text-2xl font-bold mb-4 text-center">Simple Harmonic Motion - Oscillating Spring</h3>

      {/* Visualization */}
      <div className="bg-white dark:bg-gray-800 rounded-lg p-8 mb-6 shadow-lg">
        <svg width="100%" height="300" viewBox="0 0 600 300">
          {/* Fixed point at top */}
          <rect x="0" y="0" width="600" height="20" fill="#4B5563" />

          {/* Spring */}
          <path
            d={`M 300 20 ${Array.from({ length: 20 }, (_, i) => {
              const y = 20 + (i + 1) * (130 + displacement) / 20;
              const x = 300 + (i % 2 === 0 ? 10 : -10);
              return `L ${x} ${y}`;
            }).join(' ')}`}
            stroke="#3B82F6"
            strokeWidth="3"
            fill="none"
          />

          {/* Mass */}
          <circle
            cx="300"
            cy={150 + displacement}
            r="20"
            fill="#EF4444"
            stroke="#991B1B"
            strokeWidth="2"
          />
          <text
            x="300"
            y={150 + displacement}
            textAnchor="middle"
            dy="5"
            fill="white"
            fontSize="14"
            fontWeight="bold"
          >
            m
          </text>

          {/* Equilibrium line */}
          <line
            x1="200"
            y1="150"
            x2="400"
            y2="150"
            stroke="#94A3B8"
            strokeWidth="2"
            strokeDasharray="5,5"
          />
          <text x="410" y="155" fill="#64748B" fontSize="12">Equilibrium</text>

          {/* Displacement indicator */}
          {Math.abs(displacement) > 2 && (
            <>
              <line
                x1="320"
                y1="150"
                x2="320"
                y2={150 + displacement}
                stroke="#10B981"
                strokeWidth="2"
                markerEnd="url(#arrowhead)"
              />
              <text
                x="330"
                y={(150 + (150 + displacement)) / 2}
                fill="#059669"
                fontSize="12"
              >
                x = {displacement.toFixed(1)}
              </text>
            </>
          )}

          {/* Arrow marker definition */}
          <defs>
            <marker
              id="arrowhead"
              markerWidth="10"
              markerHeight="10"
              refX="5"
              refY="5"
              orient="auto"
            >
              <polygon points="0 0, 10 5, 0 10" fill="#10B981" />
            </marker>
          </defs>
        </svg>
      </div>

      {/* Controls */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
        <div>
          <label className="block text-sm font-medium mb-2">
            Amplitude (cm): {userAmplitude.toFixed(1)}
          </label>
          <Slider
            value={[userAmplitude]}
            onValueChange={(v) => setUserAmplitude(v[0])}
            min={10}
            max={80}
            step={5}
            disabled={isPlaying}
          />
        </div>

        <div>
          <label className="block text-sm font-medium mb-2">
            Frequency (Hz): {userFrequency.toFixed(1)}
          </label>
          <Slider
            value={[userFrequency]}
            onValueChange={(v) => setUserFrequency(v[0])}
            min={0.5}
            max={3}
            step={0.1}
            disabled={isPlaying}
          />
        </div>
      </div>

      {/* Play controls */}
      <div className="flex justify-center gap-4 mb-6">
        <Button
          onClick={() => setIsPlaying(!isPlaying)}
          variant="default"
          size="lg"
        >
          {isPlaying ? <Pause className="mr-2 h-5 w-5" /> : <Play className="mr-2 h-5 w-5" />}
          {isPlaying ? 'Pause' : 'Play'}
        </Button>
        <Button
          onClick={handleReset}
          variant="outline"
          size="lg"
        >
          <RotateCcw className="mr-2 h-5 w-5" />
          Reset
        </Button>
      </div>

      {/* Data display */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 bg-white dark:bg-gray-800 rounded-lg p-4">
        <div className="text-center">
          <div className="text-sm text-gray-600 dark:text-gray-400">Displacement</div>
          <div className="text-xl font-bold text-blue-600">{displacement.toFixed(2)} cm</div>
        </div>
        <div className="text-center">
          <div className="text-sm text-gray-600 dark:text-gray-400">Velocity</div>
          <div className="text-xl font-bold text-green-600">{velocity.toFixed(2)} cm/s</div>
        </div>
        <div className="text-center">
          <div className="text-sm text-gray-600 dark:text-gray-400">Acceleration</div>
          <div className="text-xl font-bold text-purple-600">{acceleration.toFixed(2)} cm/s²</div>
        </div>
        <div className="text-center">
          <div className="text-sm text-gray-600 dark:text-gray-400">Period</div>
          <div className="text-xl font-bold text-orange-600">{(1/userFrequency).toFixed(2)} s</div>
        </div>
      </div>

      {/* Energy bars */}
      <div className="mt-6 bg-white dark:bg-gray-800 rounded-lg p-4">
        <h4 className="font-semibold mb-3">Energy Distribution</h4>
        <div className="space-y-3">
          <div>
            <div className="flex justify-between text-sm mb-1">
              <span>Kinetic Energy</span>
              <span className="font-mono">{kineticEnergy.toFixed(2)} J</span>
            </div>
            <div className="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-4">
              <div
                className="bg-green-500 h-4 rounded-full transition-all duration-100"
                style={{ width: `${(kineticEnergy / totalEnergy) * 100}%` }}
              />
            </div>
          </div>

          <div>
            <div className="flex justify-between text-sm mb-1">
              <span>Potential Energy</span>
              <span className="font-mono">{potentialEnergy.toFixed(2)} J</span>
            </div>
            <div className="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-4">
              <div
                className="bg-blue-500 h-4 rounded-full transition-all duration-100"
                style={{ width: `${(potentialEnergy / totalEnergy) * 100}%` }}
              />
            </div>
          </div>

          <div>
            <div className="flex justify-between text-sm mb-1">
              <span>Total Energy (conserved)</span>
              <span className="font-mono">{totalEnergy.toFixed(2)} J</span>
            </div>
            <div className="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-4">
              <div className="bg-purple-500 h-4 rounded-full" style={{ width: '100%' }} />
            </div>
          </div>
        </div>
      </div>

      {/* Singapore context */}
      <div className="mt-6 p-4 bg-blue-100 dark:bg-blue-900/30 rounded-lg">
        <p className="text-sm">
          <strong>🇸🇬 Singapore Application:</strong> The Marina Bay Sands SkyPark uses a
          tuned mass damper (similar to a spring-mass system) to reduce building oscillations
          during earthquakes. The damper's frequency is tuned to counteract the building's
          natural frequency!
        </p>
      </div>
    </div>
  );
}
