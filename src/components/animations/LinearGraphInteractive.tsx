import { useState } from "react";
import { motion } from "framer-motion";
import { Card } from "@/components/ui/card";
import { Slider } from "@/components/ui/slider";

interface LinearGraphInteractiveProps {
  defaultM?: number;
  defaultC?: number;
}

const LinearGraphInteractive = ({
  defaultM = 2,
  defaultC = 1
}: LinearGraphInteractiveProps) => {
  const [m, setM] = useState(defaultM);
  const [c, setC] = useState(defaultC);

  // Graph dimensions
  const width = 400;
  const height = 400;
  const scale = 30; // pixels per unit
  const originX = width / 2;
  const originY = height / 2;

  // Convert mathematical coordinates to SVG coordinates
  const toSVGCoords = (x: number, y: number) => {
    return {
      x: originX + x * scale,
      y: originY - y * scale, // Negative because SVG y increases downward
    };
  };

  // Calculate line points
  const x1 = -7;
  const y1 = m * x1 + c;
  const x2 = 7;
  const y2 = m * x2 + c;

  const point1 = toSVGCoords(x1, y1);
  const point2 = toSVGCoords(x2, y2);

  // Y-intercept point
  const yInterceptSVG = toSVGCoords(0, c);

  // Point for showing gradient (rise over run)
  const gradientX = 2;
  const gradientY1 = m * gradientX + c;
  const gradientY2 = c;
  const gradientPoint1 = toSVGCoords(gradientX, gradientY1);
  const gradientPoint2 = toSVGCoords(gradientX, gradientY2);
  const gradientPoint3 = toSVGCoords(0, c);

  return (
    <Card className="p-6 bg-gradient-to-br from-blue-50 to-indigo-50 dark:from-blue-950 dark:to-indigo-950">
      <div className="space-y-6">
        <div className="text-center">
          <h3 className="text-xl font-bold text-blue-900 dark:text-blue-100 mb-2">
            Linear Equation Grapher
          </h3>
          <p className="text-lg font-mono text-blue-700 dark:text-blue-300">
            y = {m}x {c >= 0 ? "+" : ""} {c}
          </p>
        </div>

        {/* SVG Graph */}
        <div className="flex justify-center">
          <svg
            width={width}
            height={height}
            className="border-2 border-blue-300 dark:border-blue-700 rounded-lg bg-white dark:bg-gray-900"
          >
            {/* Grid lines */}
            {Array.from({ length: 15 }, (_, i) => i - 7).map((i) => (
              <g key={`grid-${i}`}>
                {/* Vertical grid lines */}
                <line
                  x1={originX + i * scale}
                  y1={0}
                  x2={originX + i * scale}
                  y2={height}
                  stroke={i === 0 ? "#3b82f6" : "#dbeafe"}
                  strokeWidth={i === 0 ? 2 : 1}
                  opacity={i === 0 ? 1 : 0.3}
                />
                {/* Horizontal grid lines */}
                <line
                  x1={0}
                  y1={originY + i * scale}
                  x2={width}
                  y2={originY + i * scale}
                  stroke={i === 0 ? "#3b82f6" : "#dbeafe"}
                  strokeWidth={i === 0 ? 2 : 1}
                  opacity={i === 0 ? 1 : 0.3}
                />
              </g>
            ))}

            {/* Gradient triangle (rise over run) */}
            {m !== 0 && Math.abs(c) <= 6 && (
              <g>
                {/* Horizontal line (run) */}
                <motion.line
                  x1={gradientPoint3.x}
                  y1={gradientPoint3.y}
                  x2={gradientPoint2.x}
                  y2={gradientPoint2.y}
                  stroke="#f59e0b"
                  strokeWidth={2}
                  strokeDasharray="4 2"
                  initial={{ pathLength: 0 }}
                  animate={{ pathLength: 1 }}
                  transition={{ delay: 0.5, duration: 0.5 }}
                />
                {/* Vertical line (rise) */}
                <motion.line
                  x1={gradientPoint2.x}
                  y1={gradientPoint2.y}
                  x2={gradientPoint1.x}
                  y2={gradientPoint1.y}
                  stroke="#f59e0b"
                  strokeWidth={2}
                  strokeDasharray="4 2"
                  initial={{ pathLength: 0 }}
                  animate={{ pathLength: 1 }}
                  transition={{ delay: 0.7, duration: 0.5 }}
                />
                {/* Labels */}
                <text
                  x={(gradientPoint3.x + gradientPoint2.x) / 2}
                  y={gradientPoint3.y + 15}
                  fill="#f59e0b"
                  fontSize="12"
                  textAnchor="middle"
                  className="font-semibold"
                >
                  run: 2
                </text>
                <text
                  x={gradientPoint2.x + 20}
                  y={(gradientPoint2.y + gradientPoint1.y) / 2}
                  fill="#f59e0b"
                  fontSize="12"
                  textAnchor="start"
                  className="font-semibold"
                >
                  rise: {(m * 2).toFixed(1)}
                </text>
              </g>
            )}

            {/* Main line */}
            <motion.line
              x1={point1.x}
              y1={point1.y}
              x2={point2.x}
              y2={point2.y}
              stroke="#2563eb"
              strokeWidth={3}
              initial={{ pathLength: 0 }}
              animate={{ pathLength: 1 }}
              transition={{ duration: 1, ease: "easeInOut" }}
            />

            {/* Y-intercept point */}
            {Math.abs(c) <= 6 && (
              <motion.g
                initial={{ scale: 0 }}
                animate={{ scale: 1 }}
                transition={{ delay: 0.5, type: "spring" }}
              >
                <circle
                  cx={yInterceptSVG.x}
                  cy={yInterceptSVG.y}
                  r={6}
                  fill="#dc2626"
                />
                <text
                  x={yInterceptSVG.x + 12}
                  y={yInterceptSVG.y + 5}
                  fill="#dc2626"
                  fontSize="14"
                  fontWeight="bold"
                >
                  (0, {c})
                </text>
              </motion.g>
            )}

            {/* Axis labels */}
            <text x={width - 15} y={originY - 10} fill="#3b82f6" fontSize="14" fontWeight="bold">
              x
            </text>
            <text x={originX + 10} y={15} fill="#3b82f6" fontSize="14" fontWeight="bold">
              y
            </text>
          </svg>
        </div>

        {/* Controls */}
        <div className="space-y-4">
          <div>
            <label className="text-sm font-semibold text-blue-900 dark:text-blue-100">
              Gradient (m): {m}
            </label>
            <Slider
              value={[m]}
              onValueChange={([value]) => setM(value)}
              min={-3}
              max={3}
              step={0.5}
              className="mt-2"
            />
          </div>

          <div>
            <label className="text-sm font-semibold text-blue-900 dark:text-blue-100">
              Y-intercept (c): {c}
            </label>
            <Slider
              value={[c]}
              onValueChange={([value]) => setC(value)}
              min={-5}
              max={5}
              step={0.5}
              className="mt-2"
            />
          </div>
        </div>

        {/* Properties */}
        <div className="grid grid-cols-2 gap-4 text-sm">
          <div className="bg-white dark:bg-gray-800 p-3 rounded-lg">
            <p className="font-semibold text-blue-900 dark:text-blue-100">Gradient (m)</p>
            <p className="text-blue-700 dark:text-blue-300 font-mono">
              {m > 0 ? `Positive (↗ rising)` : m < 0 ? `Negative (↘ falling)` : `Zero (→ horizontal)`}
            </p>
          </div>

          <div className="bg-white dark:bg-gray-800 p-3 rounded-lg">
            <p className="font-semibold text-blue-900 dark:text-blue-100">Y-intercept (c)</p>
            <p className="text-blue-700 dark:text-blue-300 font-mono">
              (0, {c})
            </p>
          </div>

          <div className="bg-white dark:bg-gray-800 p-3 rounded-lg">
            <p className="font-semibold text-blue-900 dark:text-blue-100">Steepness</p>
            <p className="text-blue-700 dark:text-blue-300">
              {Math.abs(m) < 1 ? "Gentle" : Math.abs(m) < 2 ? "Moderate" : "Steep"}
            </p>
          </div>

          <div className="bg-white dark:bg-gray-800 p-3 rounded-lg">
            <p className="font-semibold text-blue-900 dark:text-blue-100">Equation</p>
            <p className="text-blue-700 dark:text-blue-300 font-mono text-xs">
              y = {m}x {c >= 0 ? "+" : ""} {c}
            </p>
          </div>
        </div>

        {/* Info box */}
        <div className="bg-blue-100 dark:bg-blue-900/30 p-4 rounded-lg text-sm">
          <p className="text-blue-900 dark:text-blue-100 font-semibold mb-2">
            Key Concepts:
          </p>
          <ul className="space-y-1 text-blue-800 dark:text-blue-200">
            <li>• <strong>Gradient (m)</strong>: Rise over run = change in y / change in x</li>
            <li>• <strong>Y-intercept (c)</strong>: Where the line crosses the y-axis</li>
            <li>• <strong>Parallel lines</strong>: Have the same gradient (m)</li>
            <li>• <strong>Perpendicular lines</strong>: Gradients multiply to -1 (m₁ × m₂ = -1)</li>
          </ul>
        </div>
      </div>
    </Card>
  );
};

export default LinearGraphInteractive;
