# Topic 1: Homework - Python Development

## Task 1: Factory Pattern Implementation

### Overview
In this task, we implemented the **Factory Pattern** to create vehicles with regional specifications for the US and EU markets. The goal was to design a system that could dynamically create different types of vehicles (e.g., cars and motorcycles) based on regional requirements without modifying the core vehicle classes.

### Requirements
1. **Abstract Base Class (ABC)**:
   - Implement an abstract base class `Vehicle` with a method `start_engine()`.

2. **Vehicle Subclasses**:
   - Define `Car` and `Motorcycle` classes inheriting from `Vehicle`.

3. **Abstract Factory**:
   - Create an abstract class `VehicleFactory` with methods `create_car()` and `create_motorcycle()`.

4. **Concrete Factories**:
   - Implement `USVehicleFactory` and `EUVehicleFactory` to create vehicles with "US Spec" and "EU Spec" regional details.

5. **Logging**:
   - Replace `print` statements with `logging` for INFO-level messages.

6. **Code Formatting**:
   - Format the code using `black`.

### Output Example
```text
INFO:root:Created vehicle: Ford Mustang (US Spec)
INFO:root:Ford Mustang: Engine started
INFO:root:Created vehicle: Harley-Davidson Sportster (US Spec)
INFO:root:Harley-Davidson Sportster: Engine started
INFO:root:Created vehicle: Volkswagen Golf (EU Spec)
INFO:root:Volkswagen Golf: Engine started
INFO:root:Created vehicle: BMW R1250 (EU Spec)
INFO:root:BMW R1250: Engine started
```

### Tools Used
- **Python** for implementation.
- **Logging** for structured output.
- **Black** for code formatting.

### Key Benefits of the Factory Pattern
- **Flexibility**: Easily add new regions or vehicle types without modifying existing code.
- **Scalability**: Supports expanding the system with minimal effort.
- **Code Reusability**: Promotes clean and modular code by separating creation logic.

### Conclusion
This task demonstrates how to use the Factory Pattern to dynamically create objects based on varying requirements, emphasizing the importance of design patterns in software development. The implementation adheres to the principles of clean code and type safety.

# goit-pythonweb-hw-01
