yExact = @(t) (t.^2).*log(t) + (t.^2)./2 + 1/2 + 2./t;
tspan=[1,2];
F=@(t,Y) [Y(2); 2.*Y(1)./t^2 + 3 - 1./t^2];
Y0=[3;0];
[t,Y]=ode45(F,tspan,Y0);
y=Y(:,1);

hold on;
plot(t,y,'b-x');
plot(t,yExact(t),'r-o');
hold off;
legend('Exact','Numerical');
figure;
semilogy(log(abs(y - yExact(t))),'b-x');
legend('Log of error');