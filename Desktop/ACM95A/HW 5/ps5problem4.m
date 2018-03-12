yExact = @(t) (t.^2)./4 -t./3 + 1./2 - 1./(12 .* t.^2);
tspan=[.2,2];
y0=yExact(.2);
f=@(t,y) t - 1 + 1./t -2.*y/t;
[t,y]=ode45(f,tspan,y0);
figure;
hold on;
plot(t,y,'b-x');
plot(t,yExact(t),'r-o');
hold off;
legend('Exact','Numerical');
figure;
plot(t,log(abs(y - yExact(t))),'b-x');
legend('Log of error');


