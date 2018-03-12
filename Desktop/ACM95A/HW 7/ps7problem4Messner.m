%Euler's method
dt = .025;
T = 0:.025:1;
Y = zeros(1,41);
Y(1) = 1;
for i = 2:1:41
    Y(i) = Y(i-1) + dt.*(T(i-1).^2 - Y(i-1).^2).*sin(Y(i-1));
end

%Heun's method
Y2 = zeros(1,41);
Y2(1) = 1;
for i = 2:1:41
    yn1 = Y(i-1) + dt.*(T(i-1).^2 - Y(i-1).^2).*sin(Y(i-1));
    Y2(i) = Y2(i-1) + (dt./2).*((T(i-1).^2 - Y2(i-1).^2).*sin(Y2(i-1)) + (T(i).^2 - yn1.^2).*sin(yn1));
end

%ODE 45 method
tspan=[0,1];
f=@(t,y) (t.^2 - y.^2).*sin(y);
y0 = 1;
[t,y]=ode45(f,tspan,y0);

hold on;
plot(T,Y,'r-o');
plot(T,Y2,'b-x');
plot(t,y,'g-v');
hold off;
legend('Euler method','Heun method','ODE 45');