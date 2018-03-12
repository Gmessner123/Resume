%Explicit Euler method
dt = .025;
T = 0:.025:1;
Y = zeros(1,41);
Y(1) = .5;
for i = 2:1:41
    Y(i) = Y(i-1) + dt.*(Y(i-1).^2 + 2 .* T(i-1) .* Y(i-1))./(3 + T(i-1).^2);
end

%Implicit Euler method
Y2 = zeros(1,41);
Y2(1) = .5;
for i = 2:1:41
    a = dt./(3 + T(i-1).^2);
    b = 2 .* T(i-1) .* dt./(3 + T(i-1).^2) - 1;
    c = Y2(i-1);
    Y2(i) = (-b - sqrt(b.^2 - 4 .* a .* c))./(2.* a);
end

%ODE 45 method

tspan=[0,1];
f=@(t,y) (y.^2 + 2 .* t .* y)./(3 + t.^2);
y0 = .5;
[t,y]=ode45(f,tspan,y0);

hold on;
plot(T,Y,'r-o');
plot(T,Y2,'b-x');
plot(t,y,'g-v');
hold off;
legend('Explicit euler','Implicit euler','ODE 45');