dt = .025;
T = 0:.025:1;
Y = zeros(1,41);
Y(1) = .5;
for i = 2:1:41
    k1 = (Y(i-1).^2 + 2 .*  T(i-1) .* Y(i-1))./(3 + T(i-1).^2);
    k2 = ((Y(i-1)+ k1.*dt./2).^2 + 2 .*  (T(i-1)+ dt./2) .* (Y(i-1)+ k1.*dt./2))./(3 + (T(i-1)+ dt./2).^2);
    k3 = ((Y(i-1)+ k2.*dt./2).^2 + 2 .*  (T(i-1)+ dt./2) .* (Y(i-1)+ k2.*dt./2))./(3 + (T(i-1)+ dt./2).^2);
    k4 = ((Y(i-1)+ k3.*dt).^2 + 2 .*  (T(i-1)+ dt) .* (Y(i-1)+ k3.*dt))./(3 + (T(i-1)+ dt).^2);
    Y(i) = Y(i-1) + dt.*(k1 + 2.*k2 + 2.*k3 + k4)./6;
end

yExact = @(t) (3 + t.^2) ./ (6 - t);

hold on;
plot(T,Y,'r-o');
plot(T, yExact(T),'b-x');
hold off;

plot(T,abs(yExact(T) - Y), 'r-o')