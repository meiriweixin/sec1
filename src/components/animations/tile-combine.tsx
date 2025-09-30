import { useEffect, useState } from "react";
import { motion, useAnimation } from "framer-motion";

interface TileCombineProps {
  expression?: string;
  result?: string;
}

export function TileCombine({ expression = "x + x + x", result = "3x" }: TileCombineProps) {
  const controls = useAnimation();
  const [phase, setPhase] = useState(0);

  useEffect(() => {
    const animateSequence = async () => {
      // Phase 1: Show individual tiles
      setPhase(1);
      await new Promise(resolve => setTimeout(resolve, 1000));
      
      // Phase 2: Combine tiles
      setPhase(2);
      await controls.start("combine");
      await new Promise(resolve => setTimeout(resolve, 1000));
      
      // Phase 3: Show result
      setPhase(3);
    };

    animateSequence();
  }, [controls]);

  const tileVariants = {
    initial: { scale: 1, x: 0, opacity: 1 },
    combine: {
      x: 0,
      scale: [1, 0.8, 1],
      transition: { duration: 0.8 }
    }
  };

  const resultVariants = {
    hidden: { opacity: 0, scale: 0.5 },
    visible: { 
      opacity: 1, 
      scale: 1,
      transition: { duration: 0.6 }
    }
  };

  return (
    <div className="w-full max-w-2xl mx-auto p-8 bg-lesson-bg rounded-lg">
      <div className="text-center mb-6">
        <h3 className="text-lg font-semibold text-foreground">Combining Like Terms</h3>
        <p className="text-sm text-muted-foreground">Watch how {expression} becomes {result}</p>
      </div>
      
      <div className="flex flex-col items-center space-y-8">
        {/* Original expression */}
        <div className="flex items-center space-x-4">
          {phase >= 1 && (
            <>
              <motion.div
                className="w-16 h-16 bg-primary/20 border-2 border-primary rounded-lg flex items-center justify-center font-bold text-primary"
                initial={{ opacity: 0, y: -20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.2 }}
                variants={tileVariants}
                whileHover={{ scale: 1.1 }}
              >
                x
              </motion.div>
              
              <motion.div
                className="text-2xl font-bold text-muted-foreground"
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ delay: 0.4 }}
              >
                +
              </motion.div>
              
              <motion.div
                className="w-16 h-16 bg-primary/20 border-2 border-primary rounded-lg flex items-center justify-center font-bold text-primary"
                initial={{ opacity: 0, y: -20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.6 }}
                variants={tileVariants}
                whileHover={{ scale: 1.1 }}
              >
                x
              </motion.div>
              
              <motion.div
                className="text-2xl font-bold text-muted-foreground"
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ delay: 0.8 }}
              >
                +
              </motion.div>
              
              <motion.div
                className="w-16 h-16 bg-primary/20 border-2 border-primary rounded-lg flex items-center justify-center font-bold text-primary"
                initial={{ opacity: 0, y: -20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 1.0 }}
                variants={tileVariants}
                whileHover={{ scale: 1.1 }}
              >
                x
              </motion.div>
            </>
          )}
        </div>
        
        {/* Arrow */}
        {phase >= 2 && (
          <motion.div
            className="flex flex-col items-center"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 1.5 }}
          >
            <div className="text-2xl">↓</div>
            <div className="text-sm text-muted-foreground">Combine</div>
          </motion.div>
        )}
        
        {/* Result */}
        {phase >= 3 && (
          <motion.div
            className="w-24 h-16 bg-gradient-to-br from-accent/20 to-primary/20 border-2 border-accent rounded-lg flex items-center justify-center font-bold text-accent text-xl"
            variants={resultVariants}
            initial="hidden"
            animate="visible"
            whileHover={{ scale: 1.1 }}
          >
            {result}
          </motion.div>
        )}
        
        {/* Explanation */}
        {phase >= 3 && (
          <motion.div
            className="text-center p-4 bg-muted/50 rounded-lg"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 2.5 }}
          >
            <p className="text-sm text-foreground">
              Three x terms combine to make 3x
            </p>
            <p className="text-xs text-muted-foreground mt-1">
              Coefficient: 1 + 1 + 1 = 3
            </p>
          </motion.div>
        )}
      </div>
    </div>
  );
}