# Sistem Rumah Sakit

A simple hospital management system implemented in C# demonstrating Object-Oriented Programming (OOP) concepts including inheritance, polymorphism, and encapsulation.

## Features

- **Person Hierarchy**: Base class `Orang` with derived classes `Dokter`, `Perawat`, and `Pasien`
- **Patient Types**: Specialized patient classes (`PasienAnak`, `PasienDewasa`) inheriting from `Pasien`
- **Medical Staff Management**: Track doctors and nurses with their specializations/departments
- **Hospital Management**: Central `RumahSakit` class to manage all people and display information
- **Polymorphic Display**: Each person type has custom display formatting

## Class Structure

- `Orang.cs` - Base class for all people
- `Dokter.cs` - Doctor with specialization
- `Perawat.cs` - Nurse with department
- `Pasien.cs` - Base patient class
- `PasienAnak.cs` - Child patient specialization
- `PasienDewasa.cs` - Adult patient specialization
- `TenagaMedis.cs` - Medical staff base class
- `RumahSakit.cs` - Hospital management system
- `Program.cs` - Main entry point with demonstration

## Getting Started

### Prerequisites

- [.NET SDK](https://dotnet.microsoft.com/download) (version compatible with the project)

### Running the Application

1. Clone the repository:
```bash
git clone https://github.com/GylaxDev/A_252410103018_TASKPBO.git
cd A_252410103018_TASKPBO
```

2. Run the application:
```bash
dotnet run
```

## Technologies

- C# (.NET)

## Author

**Vincent Alexander** - [@GylaxDev](https://github.com/GylaxDev)
