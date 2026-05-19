out = sim("Simulink_Model.slx");
Vabc = out.Voltages;
Iabc = out.Currents;
t = out.tout;
save("simulation_data_demo.mat","Vabc","Iabc","t")

