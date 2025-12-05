import { useState, useEffect } from 'react';
import { Play, Pause, RotateCcw } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Slider } from '@/components/ui/slider';

interface ACWaveformVisualizerProps {
  voltage?: number;
  frequency?: number;
}

export default function ACWaveformVisualizer({
  voltage = 230,
  frequency = 50
}: ACWaveformVisualizerProps) {
  const [time, setTime] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [userVoltage, setUserVoltage] = useState(voltage);
  const [userFrequency, setUserFrequency] = useState(frequency);
  const [showRMS, setShowRMS] = useState(true);
  const [showPhasor, setShowPhasor] = useState(false);

  useEffect(() => {
    if (!isPlaying) return;

    const interval = setInterval(() => {
      setTime(t => t + 0.02);
    }, 20);

    return () => clearInterval(interval);
  }, [isPlaying]);

  const handleReset = () => {
    setTime(0);
    setIsPlaying(false);
  };

  // Calculate AC values
  const omega = 2 * Math.PI * userFrequency;
  const peakVoltage = userVoltage * Math.sqrt(2);
  const instantVoltage = peakVoltage * Math.sin(omega * time);
  const rmsVoltage = userVoltage;
  const period = 1 / userFrequency;

  // Generate waveform data
  const generateWaveform = () => {
    const points: [number, number][] = [];
    const cycles = 3;
    const samplesPerCycle = 100;

    for (let i = 0; i <= cycles * samplesPerCycle; i++) {
      const t = (i / samplesPerCycle) * period;
      const v = peakVoltage * Math.sin(omega * t);
      points.push([t, v]);
    }

    return points;
  };

  const waveformPoints = generateWaveform();

  // SVG dimensions
  const svgWidth = 600;
  const svgHeight = 300;
  const graphWidth = 500;
  const graphHeight = 250;
  const marginLeft = 50;
  const marginTop = 25;

  // Scale functions
  const xScale = (t: number) => marginLeft + (t / (3 * period)) * graphWidth;
  const yScale = (v: number) => marginTop + graphHeight / 2 - (v / (peakVoltage * 1.2)) * (graphHeight / 2);

  // Current time indicator position
  const currentTimeX = xScale((time % (3 * period)));

  return (
    <div className="w-full max-w-5xl mx-auto p-6 bg-gradient-to-br from-orange-50 to-yellow-50 dark:from-gray-800 dark:to-gray-900 rounded-lg">
      <h3 className="text-2xl font-bold mb-4 text-center">AC Waveform & Phasor Diagram</h3>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Main waveform */}
        <div className="lg:col-span-2">
          <div className="bg-white dark:bg-gray-800 rounded-lg p-4">
            <h4 className="font-semibold mb-3">Voltage vs Time</h4>
            <svg width="100%" height="300" viewBox={`0 0 ${svgWidth} ${svgHeight}`}>
              {/* Axes */}
              <line
                x1={marginLeft}
                y1={marginTop}
                x2={marginLeft}
                y2={marginTop + graphHeight}
                stroke="#6B7280"
                strokeWidth="2"
              />
              <line
                x1={marginLeft}
                y1={marginTop + graphHeight / 2}
                x2={marginLeft + graphWidth}
                y2={marginTop + graphHeight / 2}
                stroke="#6B7280"
                strokeWidth="2"
              />

              {/* Grid lines */}
              {[-1, -0.5, 0.5, 1].map(factor => {
                const y = yScale(peakVoltage * factor);
                return (
                  <g key={factor}>
                    <line
                      x1={marginLeft}
                      y1={y}
                      x2={marginLeft + graphWidth}
                      y2={y}
                      stroke="#E5E7EB"
                      strokeWidth="1"
                      strokeDasharray="4,4"
                    />
                    <text
                      x={marginLeft - 10}
                      y={y + 5}
                      textAnchor="end"
                      fontSize="10"
                      fill="#6B7280"
                    >
                      {(peakVoltage * factor).toFixed(0)}V
                    </text>
                  </g>
                );
              })}

              {/* RMS lines */}
              {showRMS && (
                <>
                  <line
                    x1={marginLeft}
                    y1={yScale(rmsVoltage)}
                    x2={marginLeft + graphWidth}
                    y2={yScale(rmsVoltage)}
                    stroke="#10B981"
                    strokeWidth="1.5"
                    strokeDasharray="6,3"
                  />
                  <line
                    x1={marginLeft}
                    y1={yScale(-rmsVoltage)}
                    x2={marginLeft + graphWidth}
                    y2={yScale(-rmsVoltage)}
                    stroke="#10B981"
                    strokeWidth="1.5"
                    strokeDasharray="6,3"
                  />
                  <text
                    x={marginLeft + graphWidth - 5}
                    y={yScale(rmsVoltage) - 5}
                    textAnchor="end"
                    fontSize="12"
                    fill="#10B981"
                    fontWeight="bold"
                  >
                    V_RMS
                  </text>
                </>
              )}

              {/* Waveform */}
              <path
                d={`M ${waveformPoints.map(([t, v]) => `${xScale(t)},${yScale(v)}`).join(' L ')}`}
                stroke="#3B82F6"
                strokeWidth="2.5"
                fill="none"
              />

              {/* Current time indicator */}
              <line
                x1={currentTimeX}
                y1={marginTop}
                x2={currentTimeX}
                y2={marginTop + graphHeight}
                stroke="#EF4444"
                strokeWidth="2"
              />
              <circle
                cx={currentTimeX}
                cy={yScale(instantVoltage)}
                r="6"
                fill="#EF4444"
              />

              {/* Labels */}
              <text
                x={marginLeft + graphWidth / 2}
                y={marginTop + graphHeight + 20}
                textAnchor="middle"
                fontSize="12"
                fill="#6B7280"
              >
                Time (s)
              </text>
              <text
                x={marginLeft - 30}
                y={marginTop + graphHeight / 2}
                textAnchor="middle"
                fontSize="12"
                fill="#6B7280"
                transform={`rotate(-90, ${marginLeft - 30}, ${marginTop + graphHeight / 2})`}
              >
                Voltage (V)
              </text>
            </svg>
          </div>
        </div>

        {/* Phasor diagram */}
        <div className="lg:col-span-1">
          {showPhasor && (
            <div className="bg-white dark:bg-gray-800 rounded-lg p-4">
              <h4 className="font-semibold mb-3">Phasor Diagram</h4>
              <svg width="100%" height="250" viewBox="0 0 250 250">
                {/* Circle */}
                <circle
                  cx="125"
                  cy="125"
                  r="80"
                  fill="none"
                  stroke="#E5E7EB"
                  strokeWidth="2"
                  strokeDasharray="4,4"
                />

                {/* Axes */}
                <line x1="125" y1="25" x2="125" y2="225" stroke="#9CA3AF" strokeWidth="1" />
                <line x1="25" y1="125" x2="225" y2="125" stroke="#9CA3AF" strokeWidth="1" />

                {/* Rotating phasor */}
                <line
                  x1="125"
                  y1="125"
                  x2={125 + 80 * Math.cos(omega * time - Math.PI / 2)}
                  y2={125 + 80 * Math.sin(omega * time - Math.PI / 2)}
                  stroke="#3B82F6"
                  strokeWidth="3"
                  markerEnd="url(#phasorArrow)"
                />

                {/* Labels */}
                <text x="235" y="130" fontSize="12" fill="#6B7280">0°</text>
                <text x="115" y="20" fontSize="12" fill="#6B7280">90°</text>
                <text x="15" y="130" fontSize="12" fill="#6B7280">180°</text>
                <text x="115" y="245" fontSize="12" fill="#6B7280">270°</text>

                {/* Angle annotation */}
                <text x="125" y="165" textAnchor="middle" fontSize="14" fill="#3B82F6" fontWeight="bold">
                  {((omega * time * 180 / Math.PI) % 360).toFixed(0)}°
                </text>

                <defs>
                  <marker
                    id="phasorArrow"
                    markerWidth="10"
                    markerHeight="10"
                    refX="8"
                    refY="5"
                    orient="auto"
                  >
                    <polygon points="0 0, 10 5, 0 10" fill="#3B82F6" />
                  </marker>
                </defs>
              </svg>
            </div>
          )}

          {/* Data display */}
          <div className="bg-white dark:bg-gray-800 rounded-lg p-4 mt-4">
            <h4 className="font-semibold mb-3">Measurements</h4>
            <div className="space-y-2 text-sm">
              <div className="flex justify-between">
                <span>Peak Voltage (V₀):</span>
                <span className="font-mono font-bold">{peakVoltage.toFixed(1)} V</span>
              </div>
              <div className="flex justify-between">
                <span>RMS Voltage:</span>
                <span className="font-mono font-bold">{rmsVoltage.toFixed(1)} V</span>
              </div>
              <div className="flex justify-between">
                <span>Instant Voltage:</span>
                <span className="font-mono font-bold text-red-600">{instantVoltage.toFixed(1)} V</span>
              </div>
              <div className="flex justify-between">
                <span>Frequency:</span>
                <span className="font-mono font-bold">{userFrequency.toFixed(1)} Hz</span>
              </div>
              <div className="flex justify-between">
                <span>Period:</span>
                <span className="font-mono font-bold">{(period * 1000).toFixed(1)} ms</span>
              </div>
              <div className="flex justify-between">
                <span>Angular Freq (ω):</span>
                <span className="font-mono font-bold">{omega.toFixed(1)} rad/s</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Controls */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
        <div>
          <label className="block text-sm font-medium mb-2">
            RMS Voltage (V): {userVoltage.toFixed(0)}
          </label>
          <Slider
            value={[userVoltage]}
            onValueChange={(v) => setUserVoltage(v[0])}
            min={100}
            max={400}
            step={10}
            disabled={isPlaying}
          />
        </div>

        <div>
          <label className="block text-sm font-medium mb-2">
            Frequency (Hz): {userFrequency.toFixed(0)}
          </label>
          <Slider
            value={[userFrequency]}
            onValueChange={(v) => setUserFrequency(v[0])}
            min={25}
            max={100}
            step={5}
            disabled={isPlaying}
          />
        </div>
      </div>

      {/* Play controls */}
      <div className="flex justify-center gap-4 mt-6">
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

      {/* Display options */}
      <div className="flex justify-center gap-6 mt-4">
        <label className="flex items-center space-x-2 cursor-pointer">
          <input
            type="checkbox"
            checked={showRMS}
            onChange={(e) => setShowRMS(e.target.checked)}
            className="rounded"
          />
          <span className="text-sm">Show RMS Lines</span>
        </label>

        <label className="flex items-center space-x-2 cursor-pointer">
          <input
            type="checkbox"
            checked={showPhasor}
            onChange={(e) => setShowPhasor(e.target.checked)}
            className="rounded"
          />
          <span className="text-sm">Show Phasor Diagram</span>
        </label>
      </div>

      {/* Singapore context */}
      <div className="mt-6 grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className="p-4 bg-orange-100 dark:bg-orange-900/30 rounded-lg">
          <p className="text-sm">
            <strong>🇸🇬 Singapore Standard:</strong> Singapore's mains supply is 230V RMS at 50Hz.
            The peak voltage is actually 230 × √2 ≈ 325V!
          </p>
        </div>

        <div className="p-4 bg-yellow-100 dark:bg-yellow-900/30 rounded-lg">
          <p className="text-sm">
            <strong>Fun Fact:</strong> Singapore Power Grid operates at 50Hz precisely synchronized
            across the entire island. All power generation must maintain this exact frequency!
          </p>
        </div>
      </div>
    </div>
  );
}
