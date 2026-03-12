%% MATLAB Lab: WiFi, Bluetooth, Cellular performance analyzing
% communication_assignment.m

clear all;
close all;
clc;

%% Common parameters
G_t = 1;              % Transmit antenna gain
G_r = 1;              % Receive antenna gain
c   = 3*1e8;          % Speed of light (m/s)
Pn  = 500*1e-6;       % Noise power (W)

%% -------------------- Task 1: WiFi Simulation -------------------- %%
% Parameters
f_wifi      = 2.4*1e9;        % Hz, IEEE 802.11b
BW_wifi     = 22*1e6;         % Hz
d_wifi      = 1:5:100;        % m
P_t_wifi    = 100*1e-3;       % W
lambda_wifi = c/f_wifi;       % m

% Friis Transmission Equation (received power in linear scale)
% Pr = Pt * Gt * Gr * (lambda^2) / (4*pi*R)^2
Pr_wifi = P_t_wifi * G_t * G_r * (lambda_wifi.^2) ./ ( (4*pi*d_wifi).^2 );

% Convert to dB
Pr_wifi_dB = 10*log10(Pr_wifi);

% SINR (assuming only noise, no extra interference)
SINR_wifi      = Pr_wifi ./ Pn;          % linear
SINR_wifi_dB   = 10*log10(SINR_wifi);

% Channel capacity
% C = BW * log2(1 + SINR_linear)
C_wifi         = BW_wifi .* log2(1 + SINR_wifi);   % bits/s
C_wifi_dB      = 10*log10(C_wifi);                 % for plotting in dB

%% Plot WiFi results
figure;
subplot(3,1,1);
plot(d_wifi, Pr_wifi_dB, 'b','LineWidth',1.5);
grid on;
xlabel('Distance (m)');
ylabel('P_r (dB)');
title('WiFi: Received Power vs Distance');

subplot(3,1,2);
plot(d_wifi, SINR_wifi_dB, 'r','LineWidth',1.5);
grid on;
xlabel('Distance (m)');
ylabel('SINR (dB)');
title('WiFi: SINR vs Distance');

subplot(3,1,3);
plot(d_wifi, C_wifi_dB, 'k','LineWidth',1.5);
grid on;
xlabel('Distance (m)');
ylabel('Capacity (dB)');
title('WiFi: Capacity vs Distance');

%% ----------------- Task 2: Bluetooth Simulation ------------------ %%
% Parameters
f_bluetooth      = 2.45*1e9;      % Hz
BW_bluetooth     = 2*1e6;         % Hz
d_bluetooth      = 0.5:0.5:10;    % m
P_t_bluetooth    = 10*1e-3;       % W
lambda_bluetooth = c/f_bluetooth; % m

% Received power
Pr_bluetooth = P_t_bluetooth * G_t * G_r * (lambda_bluetooth.^2) ./ ( (4*pi*d_bluetooth).^2 );
Pr_bluetooth_dB = 10*log10(Pr_bluetooth);

% SINR
SINR_bluetooth    = Pr_bluetooth ./ Pn;
SINR_bluetooth_dB = 10*log10(SINR_bluetooth);

% Capacity
C_bluetooth    = BW_bluetooth .* log2(1 + SINR_bluetooth);
C_bluetooth_dB = 10*log10(C_bluetooth);

%% Plot Bluetooth results
figure;
subplot(3,1,1);
plot(d_bluetooth, Pr_bluetooth_dB, 'b','LineWidth',1.5);
grid on;
xlabel('Distance (m)');
ylabel('P_r (dB)');
title('Bluetooth: Received Power vs Distance');

subplot(3,1,2);
plot(d_bluetooth, SINR_bluetooth_dB, 'r','LineWidth',1.5);
grid on;
xlabel('Distance (m)');
ylabel('SINR (dB)');
title('Bluetooth: SINR vs Distance');

subplot(3,1,3);
plot(d_bluetooth, C_bluetooth_dB, 'k','LineWidth',1.5);
grid on;
xlabel('Distance (m)');
ylabel('Capacity (dB)');
title('Bluetooth: Capacity vs Distance');

%% ----------------- Task 3: Cellular Simulation ------------------- %%
% Parameters
f_cellular      = 850*1e6;        % Hz, 2G GSM
BW_cellular     = 200*1e3;        % Hz
d_cellular      = 100:100:5000;   % m
P_t_cellular    = 40;             % W
lambda_cellular = c/f_cellular;   % m

% Received power
Pr_cellular = P_t_cellular * G_t * G_r * (lambda_cellular.^2) ./ ( (4*pi*d_cellular).^2 );
Pr_cellular_dB = 10*log10(Pr_cellular);

% SINR
SINR_cellular    = Pr_cellular ./ Pn;
SINR_cellular_dB = 10*log10(SINR_cellular);

% Capacity
C_cellular    = BW_cellular .* log2(1 + SINR_cellular);
C_cellular_dB = 10*log10(C_cellular);

%% Plot Cellular results
figure;
subplot(3,1,1);
plot(d_cellular, Pr_cellular_dB, 'b','LineWidth',1.5);
grid on;
xlabel('Distance (m)');
ylabel('P_r (dB)');
title('Cellular: Received Power vs Distance');

subplot(3,1,2);
plot(d_cellular, SINR_cellular_dB, 'r','LineWidth',1.5);
grid on;
xlabel('Distance (m)');
ylabel('SINR (dB)');
title('Cellular: SINR vs Distance');

subplot(3,1,3);
plot(d_cellular, C_cellular_dB, 'k','LineWidth',1.5);
grid on;
xlabel('Distance (m)');
ylabel('Capacity (dB)');
title('Cellular: Capacity vs Distance');

%% ----------------- Task 4: Comparative Analysis ------------------ %%
% For a clearer comparison, we can plot each metric in one figure.

% 1) Received power comparison
figure;
plot(d_wifi, Pr_wifi_dB, 'b','LineWidth',1.5); hold on;
plot(d_bluetooth, Pr_bluetooth_dB, 'r','LineWidth',1.5);
plot(d_cellular, Pr_cellular_dB, 'g','LineWidth',1.5);
grid on;
xlabel('Distance (m)');
ylabel('P_r (dB)');
title('Received Power Comparison');
legend('WiFi','Bluetooth','Cellular','Location','best');

% 2) SINR comparison
figure;
plot(d_wifi, SINR_wifi_dB, 'b','LineWidth',1.5); hold on;
plot(d_bluetooth, SINR_bluetooth_dB, 'r','LineWidth',1.5);
plot(d_cellular, SINR_cellular_dB, 'g','LineWidth',1.5);
grid on;
xlabel('Distance (m)');
ylabel('SINR (dB)');
title('SINR Comparison');
legend('WiFi','Bluetooth','Cellular','Location','best');

% 3) Capacity comparison
figure;
plot(d_wifi, C_wifi_dB, 'b','LineWidth',1.5); hold on;
plot(d_bluetooth, C_bluetooth_dB, 'r','LineWidth',1.5);
plot(d_cellular, C_cellular_dB, 'g','LineWidth',1.5);
grid on;
xlabel('Distance (m)');
ylabel('Capacity (dB)');
title('Capacity Comparison');
legend('WiFi','Bluetooth','Cellular','Location','best');

