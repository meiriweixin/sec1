import { useEffect, useRef } from "react";
import { motion } from "framer-motion";

interface ParticlesInStatesProps {
  states?: string[];
}

export function ParticlesInStates({ states = ["solid", "liquid", "gas"] }: ParticlesInStatesProps) {
  const generateParticles = (state: string, count: number = 16) => {
    const particles = [];
    
    for (let i = 0; i < count; i++) {
      let x, y, motionProps;
      
      switch (state) {
        case "solid":
          // Regular grid pattern, minimal movement
          x = 20 + (i % 4) * 40;
          y = 20 + Math.floor(i / 4) * 40;
          motionProps = {
            x: [x - 2, x + 2, x - 2],
            y: [y - 2, y + 2, y - 2],
            transition: {
              duration: 2,
              repeat: Infinity,
              ease: "easeInOut"
            }
          };
          break;
          
        case "liquid":
          // More spread out, flowing movement
          x = 15 + Math.random() * 130;
          y = 15 + Math.random() * 130;
          motionProps = {
            x: [x - 10, x + 10, x - 5, x + 5, x],
            y: [y - 5, y + 5, y - 10, y + 10, y],
            transition: {
              duration: 3,
              repeat: Infinity,
              ease: "easeInOut"
            }
          };
          break;
          
        case "gas":
          // Widely spread, rapid random movement
          x = 10 + Math.random() * 140;
          y = 10 + Math.random() * 140;
          motionProps = {
            x: [x - 30, x + 30, x - 20, x + 25, x],
            y: [y - 30, y + 30, y - 25, y + 20, y],
            transition: {
              duration: 1.5,
              repeat: Infinity,
              ease: "linear"
            }
          };
          break;
          
        default:
          x = 50;
          y = 50;
          motionProps = {};
      }
      
      particles.push({
        id: i,
        x,
        y,
        motionProps
      });
    }
    
    return particles;
  };

  const getStateTitle = (state: string) => {
    switch (state) {
      case "solid": return "Solid";
      case "liquid": return "Liquid";
      case "gas": return "Gas";
      default: return state;
    }
  };

  const getStateDescription = (state: string) => {
    switch (state) {
      case "solid": return "Particles vibrate in fixed positions";
      case "liquid": return "Particles flow past each other";
      case "gas": return "Particles move freely and rapidly";
      default: return "";
    }
  };

  const getStateColor = (state: string) => {
    switch (state) {
      case "solid": return "text-blue-500";
      case "liquid": return "text-green-500";
      case "gas": return "text-red-500";
      default: return "text-primary";
    }
  };

  return (
    <div className="w-full max-w-4xl mx-auto p-8 bg-lesson-bg rounded-lg">
      <div className="text-center mb-6">
        <h3 className="text-lg font-semibold text-foreground">States of Matter</h3>
        <p className="text-sm text-muted-foreground">Observe how particles behave in different states</p>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {states.map((state, index) => {
          const particles = generateParticles(state);
          const stateColor = getStateColor(state);
          
          return (
            <motion.div
              key={state}
              className="bg-card border border-border rounded-lg p-4"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: index * 0.2 }}
            >
              <h4 className={`text-center font-semibold mb-2 ${stateColor}`}>
                {getStateTitle(state)}
              </h4>
              
              {/* Particle container */}
              <div className="relative w-full h-40 bg-muted/30 rounded border-2 border-dashed border-border overflow-hidden">
                {particles.map((particle) => (
                  <motion.div
                    key={particle.id}
                    className={`absolute w-3 h-3 rounded-full ${stateColor.replace('text-', 'bg-')}`}
                    initial={{ x: particle.x, y: particle.y, opacity: 0 }}
                    animate={{
                      opacity: 1,
                      ...particle.motionProps
                    }}
                    transition={{
                      opacity: { delay: index * 0.3 + particle.id * 0.05 },
                      ...particle.motionProps.transition
                    }}
                  />
                ))}
              </div>
              
              <p className="text-xs text-muted-foreground text-center mt-2">
                {getStateDescription(state)}
              </p>
            </motion.div>
          );
        })}
      </div>
      
      <div className="text-center mt-6 p-4 bg-muted/50 rounded-lg">
        <p className="text-sm text-foreground">
          <strong>Key Observation:</strong> As we move from solid to gas, particles gain more kinetic energy and freedom of movement.
        </p>
      </div>
    </div>
  );
}