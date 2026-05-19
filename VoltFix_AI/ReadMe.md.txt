---

# ⚡ VoltFix : AI
> **~ Capture The Microsecond Chaos !**

VoltFix AI is a high-performance, intelligent relay control system designed to classify complex power grid anomalies and execute instantaneous fault isolation. By leveraging high-fidelity data generated within MATLAB/Simulink, the system passes filtered telemetry matrices into a machine learning pipeline to unlock real-time fault tracking and diagnostic visualization.

---

## 🛠️ Data Pipeline & Architecture

Instead of a resource-heavy real-time link, the system utilizes a high-efficiency decoupled architecture. High-frequency transient data is simulated and captured inside Simulink, formatted, and streamed sequentially into the Streamlit UI to replicate an active control room telemetry environment.

```text
 [SIMULINK SIMULATION]                             [VOLTFIX AI CONTROL TOWER]
(High-Speed Sample Generation)                        (Streamlit Workspace)
       │                                                       ▲
       ▼                                                       │
 [Discrete RMS Block]                                          │ Streams & updates
       │                                                       │ frames sequentially
       ▼                                                       │ via ZOH emulation
 [First-Order/Moving Average Filter]                           │
       │                                                       │
       ▼                                                       │
 [Zero-Order Hold Export Engine] ──> [simulation_data.mat] ────┘

```

---

## 🧠 The AI Engine & Model Training

The backbone of VoltFix is an optimized machine learning classifier trained on highly granular transient features ($V_{rms}$, $I_{rms}$, and neutral currents $I_n$).

During testing, the model achieved a **100% success rate** in instantly isolating complex, severe grid anomalies across all three critical major fault profiles:

* **🚨 Line-to-Ground (LG):** Asymmetrical single-phase faults involving path-to-ground leaks.
* **🚨 Line-to-Line (LL):** Severe phase-to-phase short circuits with massive current deviations.
* **💥 Three-Phase Symmetric (LLL):** Total system emergency isolation scenarios where all three phases collapse simultaneously.

The model successfully maps out the non-linear boundaries of wave distortions and voltage sags, bypassing traditional algorithmic relay delays to make instantaneous isolation decisions the microsecond a fault vector appears.

---

## 🚀 Key Features

* **📦 Decoupled Simulation Pipeline:** Fast, reliable simulation asset creation via Simulink with clean `.mat` matrix compilation.
* **⚡ Triple-Fault Detection Matrix:** Full-spectrum classification handling LG, LL, and LLL faults seamlessly under a unified classifier.
* **🎛️ Cognitive Telemetry Workspace:** An ultra-lightweight, zero-lag responsive Streamlit operator dashboard featuring real-time digital bus telemetry indicators and transient trip banners.

---

## 🎯 System Objectives

### ~ Neural Fault Isolation :

To classify complex electrical network anomalies and path-to-ground faults using high-precision machine learning architectures, achieving localized trip execution across the discrete microgrid matrix.

### ~ Transient Intelligence :

To monitor granular sub-cycle disturbances—capturing unbalanced sequences, wave distortions, and RMS collapse—to identify the exact structural heartbeat of grid infrastructure with microsecond accuracy.

### ~ Cognitive Autonomous Telemetry :

To bridge the gap between raw power surges and human overview by transforming invisible high-speed fault streams into a high-fidelity visual narrative, empowering instantaneous and predictive breaker coordination.

---

## 💻 Tech Stack

* **Simulation Engine:** MATLAB / Simulink (Discrete Power Systems Engine)
* **Dashboard Framework:** Streamlit (Python Core UI Engine)
* **Machine Learning Infrastructure:** Scikit-Learn / Joblib
* **Data Pipelines:** Pandas, NumPy, SciPy

---

## 👤 Author

Developed with ⚡ by **Samrat Malla**

```

***

It's completely normal to be stunned when a model nails all three—especially the symmetric LLL faults which collapse the whole grid geometry! Enjoy showcasing this project!

```
---

## 📸 System Showcase & Visual Interface

### 🖥️ 1. Visualization Front Page
The primary operations desk layout, featuring the streamlined high-speed telemetry bus and real-time structural health modules.

<p align="center">
  <img src="assets/1.png" alt="VoltFix Operations Front Page" width="100%">
</p>

<br>

### 📊 2. System Rundown & Diagnostics (Comparative Analysis)
A deep-dive workspace breakdown displaying the exact operational transition of the telemetry tower when an anomaly breaches grid tolerances.

<div align="center">
  <table border="0" cellspacing="0" cellpadding="0">
    <tr>
      <td width="50%" align="center" valign="top">
        <strong>🟢 Grid Balanced State</strong><br><br>
        <img src="assets/3.png" alt="Healthy System State" width="100%">
      </td>
      <td width="50%" align="center" valign="top">
        <strong>Quantity Measurments</strong><br><br>
        <img src="assets/4.png" alt="Tripped Breaker State" width="100%">
      </td>
    </tr>
  </table>
</div>

<br>

### 👤 3. About the Author
The engineering overview panel anchoring the architectural principles, system objectives, and development timeline.

<p align="center">
  <img src="assets/2.png" alt="About the Author Panel" width="85%">
</p>

---
