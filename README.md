# 📘 Mathematical Modeling – UFAPE (2025.2)

This repository contains implementations developed for the **Mathematical Modeling** course (2025.2 semester) at UFAPE.

The projects focus on solving **Ordinary Differential Equations (ODEs)** using numerical methods such as Euler and Runge-Kutta, as well as modeling real-world systems like predator-prey dynamics.

---

## 🚩 What is Mathematical Modeling?

Mathematical modeling is the process of representing real-world phenomena using mathematical equations and structures. These models allow us to simulate, analyze, and predict the behavior of systems in areas such as physics, biology, economics, and engineering.

---

## 🚩 What is an ODE (Ordinary Differential Equation)?

An **Ordinary Differential Equation (ODE)** is an equation that involves a function and its derivatives.

In simple terms, ODEs describe how a quantity changes over time. For example:
- Population growth
- Motion of objects
- Spread of diseases

Many real-world problems cannot be solved analytically, so we use **numerical methods** to approximate solutions.

---

## 📂 Implementations

### 🔶 1. Initial Value Problem (PVI) – Numerical Methods

This implementation solves the following ODE:
y' = -y^3, y(0) = 1

The exact solution is:

y(x) = 1 / sqrt(2x + 1)



🚩 Interval:
- 0 ≤ x ≤ 5  
- Step size: h = 0.1  

### Methods used:

- **Euler Method (Explicit)**  
  A simple numerical method that approximates the solution using tangent lines.

- **Runge-Kutta Method (RK4)**  
  A more accurate method that uses multiple evaluations per step.

### Objective:

Compare:
- Exact solution
- Euler approximation
- Runge-Kutta approximation

This comparison shows how different numerical methods vary in accuracy.

---

### 🔶 2. Lotka-Volterra Model (Predator-Prey)

This implementation models the interaction between predators and prey using a system of ODEs:
x'(t) = -ax + bxy
y'(t) = dy - cxy



Where:
- x(t): number of predators  
- y(t): number of prey  

🚩 Initial conditions:
- x(0) = 4  
- y(0) = 4  

🚩 Parameters:
- a = 0.16  
- b = 0.08  
- c = 0.9  
- d = 4.5  

🚩 Interval:
- 0 ≤ t ≤ 16  
- Step size: h = 0.001  

### Method used:

- **Euler Method**

### Objective:

Simulate and visualize the population dynamics of predators and prey over time.

The results typically show oscillatory behavior, where:
- Prey population increases → predator population increases  
- Predator population increases → prey decreases  
- Cycle repeats  

---

## 📊 Outputs

- Graph comparing exact, Euler, and Runge-Kutta solutions (Implementation 1)  
- Graph showing predator vs prey populations over time (Implementation 2)  

---

## 🛠️ Technologies

- Python  
- NumPy  
- Matplotlib  

---
