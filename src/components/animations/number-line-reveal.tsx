import { useEffect, useRef } from "react";
import { motion, useAnimation } from "framer-motion";

interface NumberLineRevealProps {
  start?: number;
  end?: number;
  highlight?: number[];
}

export function NumberLineReveal({ start = -10, end = 10, highlight = [] }: NumberLineRevealProps) {
  const controls = useAnimation();
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const animateSequence = async () => {
      // Start animation sequence
      await controls.start("visible");
      
      // Highlight specific numbers if provided
      if (highlight.length > 0) {
        await new Promise(resolve => setTimeout(resolve, 1000));
        await controls.start("highlighted");
      }
    };

    animateSequence();
  }, [controls, highlight]);

  const numbers = [];
  for (let i = start; i <= end; i++) {
    numbers.push(i);
  }

  const lineVariants = {
    hidden: { pathLength: 0, opacity: 0 },
    visible: { 
      pathLength: 1, 
      opacity: 1,
      transition: { duration: 1.5 }
    }
  };

  const numberVariants = {
    hidden: { opacity: 0, y: 20 },
    visible: (i: number) => ({
      opacity: 1,
      y: 0,
      transition: { delay: 0.1 * i, duration: 0.3 }
    }),
    highlighted: {
      scale: [1, 1.3, 1],
      color: ["#000", "#3B82F6", "#000"],
      transition: { duration: 0.8, times: [0, 0.5, 1] }
    }
  };

  const tickVariants = {
    hidden: { scaleY: 0, opacity: 0 },
    visible: (i: number) => ({
      scaleY: 1,
      opacity: 1,
      transition: { delay: 0.05 * i, duration: 0.2 }
    })
  };

  return (
    <div ref={containerRef} className="w-full max-w-4xl mx-auto p-8 bg-lesson-bg rounded-lg">
      <div className="text-center mb-4">
        <h3 className="text-lg font-semibold text-foreground">Number Line</h3>
        <p className="text-sm text-muted-foreground">Watch the number line reveal</p>
      </div>
      
      <div className="relative overflow-x-auto">
        <svg
          width="100%"
          height="120"
          viewBox="0 0 800 120"
          className="w-full"
        >
          {/* Main line */}
          <motion.path
            d="M 50 60 L 750 60"
            stroke="currentColor"
            strokeWidth="2"
            fill="none"
            variants={lineVariants}
            initial="hidden"
            animate={controls}
            className="text-primary"
          />
          
          {/* Arrow */}
          <motion.path
            d="M 740 55 L 750 60 L 740 65"
            stroke="currentColor"
            strokeWidth="2"
            fill="none"
            variants={lineVariants}
            initial="hidden"
            animate={controls}
            className="text-primary"
          />
          
          {/* Tick marks and numbers */}
          {numbers.map((num, i) => {
            const x = 50 + (i * (700 / (numbers.length - 1)));
            const isHighlighted = highlight.includes(num);
            
            return (
              <g key={num}>
                {/* Tick mark */}
                <motion.line
                  x1={x}
                  y1={50}
                  x2={x}
                  y2={70}
                  stroke="currentColor"
                  strokeWidth="1"
                  variants={tickVariants}
                  initial="hidden"
                  animate={controls}
                  custom={i}
                  className="text-border"
                />
                
                {/* Number label */}
                <motion.text
                  x={x}
                  y={85}
                  textAnchor="middle"
                  className={`text-sm font-medium fill-current ${
                    isHighlighted ? 'text-primary' : 'text-foreground'
                  }`}
                  variants={numberVariants}
                  initial="hidden"
                  animate={controls}
                  custom={i}
                >
                  {num}
                </motion.text>
                
                {/* Highlight circle */}
                {isHighlighted && (
                  <motion.circle
                    cx={x}
                    cy={60}
                    r="8"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="2"
                    initial={{ scale: 0, opacity: 0 }}
                    animate={{ 
                      scale: [0, 1.2, 1], 
                      opacity: [0, 1, 1],
                      transition: { delay: 2, duration: 0.6 }
                    }}
                    className="text-primary"
                  />
                )}
              </g>
            );
          })}
        </svg>
      </div>
      
      {/* Explanation */}
      <div className="text-center mt-4">
        <p className="text-sm text-muted-foreground">
          {highlight.length > 0 && (
            <>Numbers highlighted: {highlight.join(", ")}</>
          )}
        </p>
      </div>
    </div>
  );
}