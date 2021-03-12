# python program mass and velocity to kinetic energy and momentum

# input variables
objMass = float(input("Object Mass: "))
objVelocity = float(input("Object Velocity: "))

# calculate kinetic energy
objKineticEnergy = float(.5 * objMass * (objVelocity ** 2))

# calculate momentum
objMomentum = float(objMass * objVelocity)

# output
print("Object Kinetic Energy: " + str(objKineticEnergy) + " j.")
print("Object Momentum: " + str(objMomentum) + " kg. m/s")


