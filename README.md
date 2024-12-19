# Topic 1: - Python Development

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


# Task 2: SOLID Principles in Python

## Overview
This task focuses on implementing the **SOLID principles** to design a library management system in Python. The system allows users to manage books in a library through the command line, adhering to clean code and maintainability principles.

---

## SOLID Principles Applied

### 1. **Single Responsibility Principle (SRP)**
- A new `Book` class was created to encapsulate information about a book.
- The `Library` class handles storing and managing books, while the `LibraryManager` class focuses on user interaction.

### 2. **Open/Closed Principle (OCP)**
- The `Library` class can be extended for additional functionality without modifying its existing code.
- For example, you can add persistence (e.g., saving books to a file) by extending `Library` without changing its core implementation.

### 3. **Liskov Substitution Principle (LSP)**
- `Library` implements the `LibraryInterface`. Any subclass of `LibraryInterface` can replace `Library` without breaking functionality.

### 4. **Interface Segregation Principle (ISP)**
- The `LibraryInterface` defines only the methods required for library operations (`add_book`, `remove_book`, `get_books`), ensuring that any implementing class adheres to the specific interface.

### 5. **Dependency Inversion Principle (DIP)**
- The `LibraryManager` depends on the `LibraryInterface` abstraction rather than a concrete implementation of `Library`. This allows flexibility in substituting the library implementation without affecting the manager.

---

## Features
1. **Add a Book**: Users can add books by specifying the title, author, and publication year.
2. **Remove a Book**: Users can remove books by title.
3. **View All Books**: Users can view a list of all books in the library.
4. **Exit Program**: Users can exit the application gracefully.


### Example Interaction
```
Enter command (add, remove, show, exit): add
Enter book title: The Catcher in the Rye
Enter book author: J.D. Salinger
Enter book year: 1951
Enter command (add, remove, show, exit): show
Title: The Catcher in the Rye, Author: J.D. Salinger, Year: 1951
Enter command (add, remove, show, exit): remove
Enter book title to remove: The Catcher in the Rye
Enter command (add, remove, show, exit): show
No books in the library.
Enter command (add, remove, show, exit): exit
Exiting the program. Goodbye!
```

---

## Key Benefits
1. **Clean Code**: Each class has a single responsibility, making the system easier to understand and maintain.
2. **Scalability**: The system is designed to be extended without modifying existing code.
3. **Flexibility**: Abstractions like `LibraryInterface` enable replacing or extending implementations easily.

---

## Future Improvements
1. Add persistence to store books in a file or database.
2. Support advanced search functionality (e.g., search by author or year).
3. Implement a GUI for easier interaction.

---

## Tools Used
- **Python** for implementation.
- **Logging** for structured and informative output.

---

This task demonstrates how to apply the SOLID principles to create a robust and maintainable system. The design ensures that the system is scalable and adheres to clean code practices.
