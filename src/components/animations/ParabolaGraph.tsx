import { useState } from "react";
import { motion } from "framer-motion";
import { Card } from "@/components/ui/card";
import { Slider } from "@/components/ui/slider";

interface ParabolaGraphProps {
  defaultA?: number;
  defaultB?: number;
  defaultC?: number;
}

const ParabolaGraph = ({
  defaultA = 1,
  defaultB = 0,
  defaultC = 0
}: ParabolaGraphProps) => {
  const [a, setA] = useState(defaultA);
  const [b, setB] = useState(defaultB);
  const [c, setC] = useState(defaultC);

  // Graph dimensions
  const width = 400;
  const height = 400;
  const scale = 20; // pixels per unit
  const originX = width / 2;
  const originY = height / 2;

  // Generate parabola points
  const generateParabolaPoints = () => {
    const points: { x: number; y: number }[] = [];
    for (let x = -10; x <= 10; x += 0.2) {
      const y = a * x * x + b * x + c;
      if (Math.abs(y) <= 10) {
        points.push({ x, y });
      }
    }
    return points;
  };

  // Convert mathematical coordinates to SVG coordinates
  const toSVGCoords = (x: number, y: number) => {
    return {
      x: originX + x * scale,
      y: originY - y * scale, // Negative because SVG y increases downward
    };
  };

  // Calculate vertex
  const vertexX = -b / (2 * a);
  const vertexY = a * vertexX * vertexX + b * vertexX + c;

  // Calculate roots (if they exist)
  const discriminant = b * b - 4 * a * c;
  const hasRoots = discriminant >= 0;
  const root1 = hasRoots ? (-b + Math.sqrt(discriminant)) / (2 * a) : null;
  const root2 = hasRoots ? (-b - Math.sqrt(discriminant)) / (2 * a) : null;

  // Generate SVG path for parabola
  const points = generateParabolaPoints();
  const pathData = points
    .map((p, i) => {
      const svg = toSVGCoords(p.x, p.y);
      return `${i === 0 ? "M" : "L"} ${svg.x} ${svg.y}`;
    })
    .join(" ");

  const vertexSVG = toSVGCoords(vertexX, vertexY);

  return (
    <Card className="p-6 bg-gradient-to-br from-purple-50 to-pink-50 dark:from-purple-950 dark:to-pink-950">
      <div className="space-y-6">
        <div className="text-center">
          <h3 className="text-xl font-bold text-purple-900 dark:text-purple-100 mb-2">
            Quadratic Function Grapher
          </h3>
          <p className="text-lg font-mono text-purple-700 dark:text-purple-300">
            y = {a}x² {b >= 0 ? "+" : ""} {b}x {c >= 0 ? "+" : ""} {c}
          </p>
        </div>

        {/* SVG Graph */}
        <div className="flex justify-center">
          <svg
            width={width}
            height={height}
            className="border-2 border-purple-300 dark:border-purple-700 rounded-lg bg-white dark:bg-gray-900"
          >
            {/* Grid lines */}
            {Array.from({ length: 21 }, (_, i) => i - 10).map((i) => (
              <g key={`grid-${i}`}>
                {/* Vertical grid lines */}
                <line
                  x1={originX + i * scale}
                  y1={0}
                  x2={originX + i * scale}
                  y2={height}
                  stroke={i === 0 ? "#9333ea" : "#e9d5ff"}
                  strokeWidth={i === 0 ? 2 : 1}
                  opacity={i === 0 ? 1 : 0.3}
                />
                {/* Horizontal grid lines */}
                <line
                  x1={0}
                  y1={originY + i * scale}
                  x2={width}
                  y2={originY + i * scale}
                  stroke={i === 0 ? "#9333ea" : "#e9d5ff"}
                  strokeWidth={i === 0 ? 2 : 1}
                  opacity={i === 0 ? 1 : 0.3}
                />
              </g>
            ))}

            {/* Parabola */}
            {points.length > 0 && (
              <motion.path
                d={pathData}
                stroke="#c026d3"
                strokeWidth={3}
                fill="none"
                initial={{ pathLength: 0 }}
                animate={{ pathLength: 1 }}
                transition={{ duration: 1, ease: "easeInOut" }}
              />
            )}

            {/* Vertex point */}
            {Math.abs(vertexY) <= 10 && (
              <motion.circle
                cx={vertexSVG.x}
                cy={vertexSVG.y}
                r={6}
                fill="#db2777"
                initial={{ scale: 0 }}
                animate={{ scale: 1 }}
                transition={{ delay: 0.5, type: "spring" }}
              />
            )}

            {/* Root points */}
            {hasRoots && root1 !== null && Math.abs(root1) <= 10 && (
              <motion.circle
                cx={toSVGCoords(root1, 0).x}
                cy={toSVGCoords(root1, 0).y}
                r={5}
                fill="#10b981"
                initial={{ scale: 0 }}
                animate={{ scale: 1 }}
                transition={{ delay: 0.7, type: "spring" }}
              />
            )}
            {hasRoots && root2 !== null && Math.abs(root2) <= 10 && root1 !== root2 && (
              <motion.circle
                cx={toSVGCoords(root2, 0).x}
                cy={toSVGCoords(root2, 0).y}
                r={5}
                fill="#10b981"
                initial={{ scale: 0 }}
                animate={{ scale: 1 }}
                transition={{ delay: 0.7, type: "spring" }}
              />
            )}
          </svg>
        </div>

        {/* Controls */}
        <div className="space-y-4">
          <div>
            <label className="text-sm font-semibold text-purple-900 dark:text-purple-100">
              Coefficient a: {a}
            </label>
            <Slider
              value={[a]}
              onValueChange={([value]) => setA(value)}
              min={-3}
              max={3}
              step={0.5}
              className="mt-2"
            />
          </div>

          <div>
            <label className="text-sm font-semibold text-purple-900 dark:text-purple-100">
              Coefficient b: {b}
            </label>
            <Slider
              value={[b]}
              onValueChange={([value]) => setB(value)}
              min={-5}
              max={5}
              step={0.5}
              className="mt-2"
            />
          </div>

          <div>
            <label className="text-sm font-semibold text-purple-900 dark:text-purple-100">
              Coefficient c: {c}
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
            <p className="font-semibold text-purple-900 dark:text-purple-100">Vertex</p>
            <p className="text-purple-700 dark:text-purple-300 font-mono">
              ({vertexX.toFixed(2)}, {vertexY.toFixed(2)})
            </p>
          </div>

          <div className="bg-white dark:bg-gray-800 p-3 rounded-lg">
            <p className="font-semibold text-purple-900 dark:text-purple-100">Opens</p>
            <p className="text-purple-700 dark:text-purple-300">
              {a > 0 ? "Upward ∪" : a < 0 ? "Downward ∩" : "—"}
            </p>
          </div>

          <div className="bg-white dark:bg-gray-800 p-3 rounded-lg">
            <p className="font-semibold text-purple-900 dark:text-purple-100">Y-intercept</p>
            <p className="text-purple-700 dark:text-purple-300 font-mono">
              (0, {c})
            </p>
          </div>

          <div className="bg-white dark:bg-gray-800 p-3 rounded-lg">
            <p className="font-semibold text-purple-900 dark:text-purple-100">Roots</p>
            <p className="text-purple-700 dark:text-purple-300 font-mono text-xs">
              {hasRoots
                ? root1 === root2
                  ? `x = ${root1?.toFixed(2)}`
                  : `x = ${root1?.toFixed(2)}, ${root2?.toFixed(2)}`
                : "No real roots"}
            </p>
          </div>
        </div>
      </div>
    </Card>
  );
};

export default ParabolaGraph;
