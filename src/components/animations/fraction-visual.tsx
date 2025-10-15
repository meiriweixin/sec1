import { useState } from "react";
import { motion } from "framer-motion";
import { Button } from "@/components/ui/button";
import { Slider } from "@/components/ui/slider";

interface FractionVisualProps {
  initialNumerator?: number;
  initialDenominator?: number;
  showEquivalent?: boolean;
}

export function FractionVisual({ 
  initialNumerator = 3, 
  initialDenominator = 4,
  showEquivalent = true
}: FractionVisualProps) {
  const [numerator, setNumerator] = useState(initialNumerator);
  const [denominator, setDenominator] = useState(initialDenominator);
  const [showDecimal, setShowDecimal] = useState(false);
  const [showPercentage, setShowPercentage] = useState(false);

  const decimal = numerator / denominator;
  const percentage = decimal * 100;

  // Generate equivalent fractions
  const getEquivalentFractions = () => {
    const gcd = (a: number, b: number): number => b === 0 ? a : gcd(b, a % b);
    const divisor = gcd(numerator, denominator);
    const simplified = { num: numerator / divisor, den: denominator / divisor };
    
    const equivalents = [];
    for (let i = 1; i <= 3; i++) {
      if (i !== divisor) {
        equivalents.push({
          num: simplified.num * i,
          den: simplified.den * i
        });
      }
    }
    return equivalents;
  };

  const equivalents = showEquivalent ? getEquivalentFractions() : [];

  return (
    <div className="w-full max-w-3xl mx-auto p-8 bg-lesson-bg rounded-lg">
      <div className="text-center mb-6">
        <h3 className="text-lg font-semibold text-foreground">Fraction Visualization</h3>
        <p className="text-sm text-muted-foreground">
          Explore fractions with visual representations
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        {/* Visual Representations */}
        <div className="space-y-6">
          {/* Circle/Pie Chart */}
          <div className="bg-card p-4 rounded-lg border border-border">
            <h4 className="text-sm font-medium mb-3">Pie Chart</h4>
            <div className="flex justify-center">
              <svg width="150" height="150" viewBox="0 0 150 150">
                <circle
                  cx="75"
                  cy="75"
                  r="60"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2"
                  className="text-border"
                />
                {Array.from({ length: denominator }).map((_, i) => {
                  const angle = (360 / denominator) * i - 90;
                  const x = 75 + 60 * Math.cos((angle * Math.PI) / 180);
                  const y = 75 + 60 * Math.sin((angle * Math.PI) / 180);
                  return (
                    <line
                      key={i}
                      x1="75"
                      y1="75"
                      x2={x}
                      y2={y}
                      stroke="currentColor"
                      strokeWidth="1"
                      className="text-border"
                    />
                  );
                })}
                <motion.path
                  d={`M 75 75 L 75 15 A 60 60 0 ${numerator / denominator > 0.5 ? 1 : 0} 1 ${
                    75 + 60 * Math.cos(((360 * numerator / denominator - 90) * Math.PI) / 180)
                  } ${
                    75 + 60 * Math.sin(((360 * numerator / denominator - 90) * Math.PI) / 180)
                  } Z`}
                  fill="currentColor"
                  className="text-primary"
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 0.8 }}
                  transition={{ duration: 0.5 }}
                />
              </svg>
            </div>
          </div>

          {/* Bar/Rectangle */}
          <div className="bg-card p-4 rounded-lg border border-border">
            <h4 className="text-sm font-medium mb-3">Bar Representation</h4>
            <div className="flex space-x-1">
              {Array.from({ length: denominator }).map((_, i) => (
                <motion.div
                  key={i}
                  className={`h-12 flex-1 border ${
                    i < numerator
                      ? 'bg-primary border-primary'
                      : 'bg-muted border-border'
                  }`}
                  initial={{ scaleY: 0 }}
                  animate={{ scaleY: 1 }}
                  transition={{ delay: i * 0.05 }}
                  style={{ originY: 'bottom' }}
                />
              ))}
            </div>
          </div>

          {/* Grid */}
          <div className="bg-card p-4 rounded-lg border border-border">
            <h4 className="text-sm font-medium mb-3">Grid Representation</h4>
            <div className="grid grid-cols-5 gap-1 max-w-[200px] mx-auto">
              {Array.from({ length: Math.max(20, denominator) }).map((_, i) => {
                const isShaded = i < Math.floor((numerator / denominator) * Math.max(20, denominator));
                return (
                  <motion.div
                    key={i}
                    className={`aspect-square border ${
                      isShaded
                        ? 'bg-primary border-primary'
                        : 'bg-muted border-border'
                    }`}
                    initial={{ scale: 0 }}
                    animate={{ scale: 1 }}
                    transition={{ delay: i * 0.01 }}
                  />
                );
              })}
            </div>
          </div>
        </div>

        {/* Controls and Information */}
        <div className="space-y-6">
          {/* Fraction Display */}
          <div className="bg-gradient-to-br from-primary/10 to-accent/10 p-6 rounded-lg text-center">
            <div className="text-4xl font-bold">
              <span className="text-primary">{numerator}</span>
              <span className="text-muted-foreground mx-2">/</span>
              <span className="text-accent">{denominator}</span>
            </div>
            {showDecimal && (
              <motion.div
                initial={{ opacity: 0, y: -10 }}
                animate={{ opacity: 1, y: 0 }}
                className="mt-2 text-lg text-muted-foreground"
              >
                = {decimal.toFixed(4)}
              </motion.div>
            )}
            {showPercentage && (
              <motion.div
                initial={{ opacity: 0, y: -10 }}
                animate={{ opacity: 1, y: 0 }}
                className="mt-1 text-lg text-muted-foreground"
              >
                = {percentage.toFixed(2)}%
              </motion.div>
            )}
          </div>

          {/* Controls */}
          <div className="space-y-4">
            <div>
              <label className="text-sm font-medium">Numerator: {numerator}</label>
              <Slider
                value={[numerator]}
                onValueChange={(value) => setNumerator(value[0])}
                max={Math.max(denominator, 10)}
                min={0}
                step={1}
                className="mt-2"
              />
            </div>
            <div>
              <label className="text-sm font-medium">Denominator: {denominator}</label>
              <Slider
                value={[denominator]}
                onValueChange={(value) => value[0] > 0 && setDenominator(value[0])}
                max={20}
                min={1}
                step={1}
                className="mt-2"
              />
            </div>
          </div>

          {/* Display Options */}
          <div className="flex flex-wrap gap-2">
            <Button
              variant={showDecimal ? "default" : "outline"}
              size="sm"
              onClick={() => setShowDecimal(!showDecimal)}
            >
              Decimal
            </Button>
            <Button
              variant={showPercentage ? "default" : "outline"}
              size="sm"
              onClick={() => setShowPercentage(!showPercentage)}
            >
              Percentage
            </Button>
          </div>

          {/* Equivalent Fractions */}
          {showEquivalent && equivalents.length > 0 && (
            <div className="bg-muted/50 p-4 rounded-lg">
              <h4 className="text-sm font-medium mb-2">Equivalent Fractions:</h4>
              <div className="flex flex-wrap gap-3">
                {equivalents.slice(0, 3).map((eq, i) => (
                  <motion.div
                    key={i}
                    initial={{ opacity: 0, scale: 0.8 }}
                    animate={{ opacity: 1, scale: 1 }}
                    transition={{ delay: i * 0.1 }}
                    className="text-sm"
                  >
                    <span className="font-mono">
                      {eq.num}/{eq.den}
                    </span>
                  </motion.div>
                ))}
              </div>
            </div>
          )}

          {/* Fraction Type */}
          <div className="text-sm text-muted-foreground text-center p-3 bg-muted/30 rounded">
            {numerator === 0 && "Zero"}
            {numerator > 0 && numerator < denominator && "Proper Fraction"}
            {numerator === denominator && "Whole Number (1)"}
            {numerator > denominator && "Improper Fraction"}
          </div>
        </div>
      </div>
    </div>
  );
}












