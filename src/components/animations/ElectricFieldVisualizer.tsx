import { useState } from 'react';
import { Plus, Minus, Trash2 } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { RadioGroup, RadioGroupItem } from '@/components/ui/radio-group';
import { Label } from '@/components/ui/label';

interface Charge {
  id: number;
  x: number;
  y: number;
  charge: number; // +1 or -1
}

export default function ElectricFieldVisualizer() {
  const [charges, setCharges] = useState<Charge[]>([
    { id: 1, x: 200, y: 200, charge: 1 },
    { id: 2, x: 400, y: 200, charge: -1 }
  ]);
  const [selectedCharge, setSelectedCharge] = useState<'positive' | 'negative'>('positive');
  const [showFieldLines, setShowFieldLines] = useState(true);
  const [showEquipotentials, setShowEquipotentials] = useState(false);
  const [nextId, setNextId] = useState(3);

  const width = 600;
  const height = 400;

  const handleCanvasClick = (e: React.MouseEvent<SVGSVGElement>) => {
    const svg = e.currentTarget;
    const rect = svg.getBoundingClientRect();
    const x = ((e.clientX - rect.left) / rect.width) * width;
    const y = ((e.clientY - rect.top) / rect.height) * height;

    setCharges([...charges, {
      id: nextId,
      x,
      y,
      charge: selectedCharge === 'positive' ? 1 : -1
    }]);
    setNextId(nextId + 1);
  };

  const removeCharge = (id: number) => {
    setCharges(charges.filter(c => c.id !== id));
  };

  const clearAll = () => {
    setCharges([]);
  };

  // Calculate electric field at a point
  const getElectricField = (x: number, y: number): { ex: number; ey: number; magnitude: number } => {
    let ex = 0;
    let ey = 0;

    charges.forEach(charge => {
      const dx = x - charge.x;
      const dy = y - charge.y;
      const r2 = dx * dx + dy * dy;
      if (r2 < 100) return; // Too close to charge

      const r = Math.sqrt(r2);
      const k = 1; // Simplified constant
      const fieldMag = (k * charge.charge) / r2;

      ex += fieldMag * (dx / r);
      ey += fieldMag * (dy / r);
    });

    const magnitude = Math.sqrt(ex * ex + ey * ey);
    return { ex, ey, magnitude };
  };

  // Generate field lines
  const generateFieldLine = (startX: number, startY: number, forward: boolean) => {
    const points = [[startX, startY]];
    let x = startX;
    let y = startY;
    const step = forward ? 5 : -5;
    const maxSteps = 100;

    for (let i = 0; i < maxSteps; i++) {
      const { ex, ey, magnitude } = getElectricField(x, y);
      if (magnitude < 0.001) break;

      const dx = (forward ? ex : -ex) / magnitude * step;
      const dy = (forward ? ey : -ey) / magnitude * step;

      x += dx;
      y += dy;

      if (x < 0 || x > width || y < 0 || y > height) break;

      // Check if too close to any charge
      const tooClose = charges.some(charge => {
        const dist2 = (x - charge.x) ** 2 + (y - charge.y) ** 2;
        return dist2 < 400;
      });
      if (tooClose) break;

      points.push([x, y]);
    }

    return points;
  };

  // Generate field lines starting from each positive charge
  const fieldLines: number[][][] = [];
  if (showFieldLines) {
    charges.filter(c => c.charge > 0).forEach(charge => {
      for (let angle = 0; angle < 2 * Math.PI; angle += Math.PI / 8) {
        const startX = charge.x + Math.cos(angle) * 25;
        const startY = charge.y + Math.sin(angle) * 25;
        const line = generateFieldLine(startX, startY, true);
        if (line.length > 3) fieldLines.push(line);
      }
    });
  }

  return (
    <div className="w-full max-w-4xl mx-auto p-6 bg-gradient-to-br from-yellow-50 to-blue-50 dark:from-gray-800 dark:to-gray-900 rounded-lg">
      <h3 className="text-2xl font-bold mb-4 text-center">Interactive Electric Field Visualizer</h3>

      <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
        {/* Controls */}
        <div className="lg:col-span-1 space-y-4">
          <div className="bg-white dark:bg-gray-800 rounded-lg p-4 space-y-4">
            <h4 className="font-semibold">Add Charges</h4>

            <RadioGroup value={selectedCharge} onValueChange={(v) => setSelectedCharge(v as 'positive' | 'negative')}>
              <div className="flex items-center space-x-2">
                <RadioGroupItem value="positive" id="positive" />
                <Label htmlFor="positive" className="flex items-center gap-2 cursor-pointer">
                  <Plus className="h-4 w-4 text-red-500" />
                  Positive
                </Label>
              </div>
              <div className="flex items-center space-x-2">
                <RadioGroupItem value="negative" id="negative" />
                <Label htmlFor="negative" className="flex items-center gap-2 cursor-pointer">
                  <Minus className="h-4 w-4 text-blue-500" />
                  Negative
                </Label>
              </div>
            </RadioGroup>

            <p className="text-xs text-gray-600 dark:text-gray-400">
              Click on the canvas to place charges
            </p>

            <Button
              onClick={clearAll}
              variant="destructive"
              size="sm"
              className="w-full"
              disabled={charges.length === 0}
            >
              <Trash2 className="mr-2 h-4 w-4" />
              Clear All
            </Button>
          </div>

          <div className="bg-white dark:bg-gray-800 rounded-lg p-4 space-y-3">
            <h4 className="font-semibold">Visualization</h4>

            <label className="flex items-center space-x-2 cursor-pointer">
              <input
                type="checkbox"
                checked={showFieldLines}
                onChange={(e) => setShowFieldLines(e.target.checked)}
                className="rounded"
              />
              <span className="text-sm">Field Lines</span>
            </label>

            <label className="flex items-center space-x-2 cursor-pointer">
              <input
                type="checkbox"
                checked={showEquipotentials}
                onChange={(e) => setShowEquipotentials(e.target.checked)}
                className="rounded"
              />
              <span className="text-sm">Equipotentials</span>
            </label>
          </div>

          <div className="bg-white dark:bg-gray-800 rounded-lg p-4">
            <h4 className="font-semibold mb-2">Charges</h4>
            <div className="space-y-2 max-h-48 overflow-y-auto">
              {charges.length === 0 && (
                <p className="text-sm text-gray-500">No charges placed</p>
              )}
              {charges.map(charge => (
                <div key={charge.id} className="flex items-center justify-between text-sm">
                  <span className="flex items-center gap-2">
                    {charge.charge > 0 ? (
                      <Plus className="h-4 w-4 text-red-500" />
                    ) : (
                      <Minus className="h-4 w-4 text-blue-500" />
                    )}
                    ({charge.x.toFixed(0)}, {charge.y.toFixed(0)})
                  </span>
                  <Button
                    onClick={() => removeCharge(charge.id)}
                    variant="ghost"
                    size="sm"
                    className="h-6 w-6 p-0"
                  >
                    ×
                  </Button>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Canvas */}
        <div className="lg:col-span-3">
          <div className="bg-white dark:bg-gray-800 rounded-lg p-4">
            <svg
              width="100%"
              height="400"
              viewBox={`0 0 ${width} ${height}`}
              className="border-2 border-gray-200 dark:border-gray-700 rounded cursor-crosshair"
              onClick={handleCanvasClick}
            >
              {/* Background grid */}
              <defs>
                <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
                  <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#E5E7EB" strokeWidth="0.5" />
                </pattern>
              </defs>
              <rect width={width} height={height} fill="url(#grid)" />

              {/* Field lines */}
              {showFieldLines && fieldLines.map((line, i) => (
                <path
                  key={`line-${i}`}
                  d={`M ${line.map(p => p.join(',')).join(' L ')}`}
                  stroke="#10B981"
                  strokeWidth="1.5"
                  fill="none"
                  opacity="0.6"
                  markerEnd="url(#arrow)"
                />
              ))}

              {/* Equipotential lines (simplified) */}
              {showEquipotentials && charges.map((charge, i) => (
                <g key={`equipot-${i}`}>
                  {[30, 50, 70, 90].map(r => (
                    <circle
                      key={r}
                      cx={charge.x}
                      cy={charge.y}
                      r={r}
                      fill="none"
                      stroke={charge.charge > 0 ? "#EF4444" : "#3B82F6"}
                      strokeWidth="1"
                      strokeDasharray="4,4"
                      opacity="0.3"
                    />
                  ))}
                </g>
              ))}

              {/* Charges */}
              {charges.map(charge => (
                <g key={charge.id}>
                  <circle
                    cx={charge.x}
                    cy={charge.y}
                    r="20"
                    fill={charge.charge > 0 ? "#EF4444" : "#3B82F6"}
                    stroke={charge.charge > 0 ? "#991B1B" : "#1E40AF"}
                    strokeWidth="2"
                  />
                  <text
                    x={charge.x}
                    y={charge.y}
                    textAnchor="middle"
                    dy="7"
                    fill="white"
                    fontSize="24"
                    fontWeight="bold"
                  >
                    {charge.charge > 0 ? '+' : '−'}
                  </text>
                </g>
              ))}

              {/* Arrow marker for field lines */}
              <defs>
                <marker
                  id="arrow"
                  markerWidth="8"
                  markerHeight="8"
                  refX="6"
                  refY="4"
                  orient="auto"
                  markerUnits="strokeWidth"
                >
                  <path d="M0,0 L0,8 L8,4 z" fill="#10B981" />
                </marker>
              </defs>
            </svg>
          </div>

          {/* Information */}
          <div className="mt-4 grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="bg-blue-100 dark:bg-blue-900/30 rounded-lg p-3">
              <h5 className="font-semibold mb-1 text-sm">Field Line Rules</h5>
              <ul className="text-xs space-y-1">
                <li>• Start from + charges, end at − charges</li>
                <li>• Never cross each other</li>
                <li>• Perpendicular to equipotential surfaces</li>
                <li>• Denser lines = stronger field</li>
              </ul>
            </div>

            <div className="bg-green-100 dark:bg-green-900/30 rounded-lg p-3">
              <h5 className="font-semibold mb-1 text-sm">🇸🇬 Singapore Application</h5>
              <p className="text-xs">
                Lightning rods at Singapore's tall buildings (like Marina Bay Sands) create
                strong electric fields at their tips to attract lightning safely!
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
