import { useState, useEffect } from "react";
import { motion, useAnimation } from "framer-motion";
import { Button } from "@/components/ui/button";
import { Slider } from "@/components/ui/slider";

interface EquationBalanceProps {
  leftSide?: string;
  rightSide?: string;
  solution?: number;
}

export function EquationBalance({ 
  leftSide = "2x + 3", 
  rightSide = "11", 
  solution = 4 
}: EquationBalanceProps) {
  const controls = useAnimation();
  const [xValue, setXValue] = useState(0);
  const [isBalanced, setIsBalanced] = useState(false);
  const [showSolution, setShowSolution] = useState(false);

  const evaluateExpression = (expr: string, x: number): number => {
    // Simple evaluation for expressions like "2x + 3"
    return expr.split('+').reduce((sum, term) => {
      term = term.trim();
      if (term.includes('x')) {
        const coefficient = term.replace('x', '').trim() || '1';
        return sum + (parseFloat(coefficient) * x);
      }
      return sum + parseFloat(term);
    }, 0);
  };

  const leftValue = evaluateExpression(leftSide, xValue);
  const rightValue = parseFloat(rightSide);
  const difference = Math.abs(leftValue - rightValue);
  const balanced = difference < 0.1;

  useEffect(() => {
    setIsBalanced(balanced);
    if (balanced) {
      controls.start({
        scale: [1, 1.1, 1],
        transition: { duration: 0.5 }
      });
    }
  }, [balanced, controls]);

  const getRotation = () => {
    if (leftValue > rightValue) return -10;
    if (leftValue < rightValue) return 10;
    return 0;
  };

  return (
    <div className="w-full max-w-2xl mx-auto p-8 bg-lesson-bg rounded-lg">
      <div className="text-center mb-6">
        <h3 className="text-lg font-semibold text-foreground">Equation Balance</h3>
        <p className="text-sm text-muted-foreground">
          Find the value of x that balances the equation
        </p>
        <div className="mt-4 text-2xl font-mono">
          {leftSide} = {rightSide}
        </div>
      </div>

      {/* Balance Scale */}
      <div className="relative h-64 mb-8">
        <svg
          width="100%"
          height="100%"
          viewBox="0 0 400 200"
          className="w-full"
        >
          {/* Fulcrum */}
          <polygon
            points="200,150 180,180 220,180"
            fill="currentColor"
            className="text-muted-foreground"
          />
          
          {/* Balance Beam */}
          <motion.rect
            x="50"
            y="145"
            width="300"
            height="10"
            fill="currentColor"
            className="text-foreground"
            animate={{ rotate: getRotation() }}
            style={{ originX: "200px", originY: "150px" }}
            transition={{ type: "spring", stiffness: 100 }}
          />
          
          {/* Left Pan */}
          <motion.g
            animate={{ 
              y: leftValue > rightValue ? 10 : leftValue < rightValue ? -10 : 0,
              rotate: getRotation()
            }}
            style={{ originX: "200px", originY: "150px" }}
            transition={{ type: "spring", stiffness: 100 }}
          >
            <rect
              x="70"
              y="120"
              width="60"
              height="25"
              fill="currentColor"
              className={`${isBalanced ? 'text-success' : 'text-primary'}`}
              opacity="0.8"
              rx="4"
            />
            <text
              x="100"
              y="137"
              textAnchor="middle"
              className="fill-primary-foreground text-sm font-bold"
            >
              {leftValue.toFixed(1)}
            </text>
          </motion.g>
          
          {/* Right Pan */}
          <motion.g
            animate={{ 
              y: rightValue > leftValue ? 10 : rightValue < leftValue ? -10 : 0,
              rotate: getRotation()
            }}
            style={{ originX: "200px", originY: "150px" }}
            transition={{ type: "spring", stiffness: 100 }}
          >
            <rect
              x="270"
              y="120"
              width="60"
              height="25"
              fill="currentColor"
              className={`${isBalanced ? 'text-success' : 'text-accent'}`}
              opacity="0.8"
              rx="4"
            />
            <text
              x="300"
              y="137"
              textAnchor="middle"
              className="fill-accent-foreground text-sm font-bold"
            >
              {rightValue}
            </text>
          </motion.g>
        </svg>
      </div>

      {/* Controls */}
      <div className="space-y-4">
        <div className="space-y-2">
          <div className="flex justify-between text-sm">
            <span>x = {xValue}</span>
            <span className={`font-medium ${isBalanced ? 'text-success' : 'text-muted-foreground'}`}>
              {isBalanced ? '✓ Balanced!' : `Difference: ${difference.toFixed(1)}`}
            </span>
          </div>
          <Slider
            value={[xValue]}
            onValueChange={(value) => setXValue(value[0])}
            max={10}
            min={-10}
            step={0.1}
            className="w-full"
          />
        </div>

        <div className="flex justify-center space-x-4">
          <Button
            variant="outline"
            onClick={() => setXValue(0)}
          >
            Reset
          </Button>
          <Button
            onClick={() => setShowSolution(!showSolution)}
            className="btn-primary"
          >
            {showSolution ? 'Hide' : 'Show'} Solution
          </Button>
        </div>

        {/* Solution */}
        {showSolution && (
          <motion.div
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            className="p-4 bg-muted/50 rounded-lg text-center"
          >
            <p className="text-sm font-medium mb-2">Solution: x = {solution}</p>
            <p className="text-xs text-muted-foreground">
              When x = {solution}: {leftSide.replace('x', solution.toString())} = {leftValue} = {rightSide}
            </p>
          </motion.div>
        )}
      </div>
    </div>
  );
}



