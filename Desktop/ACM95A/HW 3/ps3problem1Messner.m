r = zeros([29]);
a = zeros([29]);
b = zeros([29]);
for R = 2:30
    argument = @(theta) (-1i*R.*exp(1i*theta)).*((R.*exp(1i*theta)) + log(R * exp(1i*theta)))./((R * exp(1i*theta)).^3 + 1);
    B = abs(integral(argument,-pi/2, pi/2));
    A = pi*R.*(R + log(R) + pi/2)./(R^3 - 1);
    a(R - 1) = A;
    b(R - 1) = B;
    r(R - 1) = R;
end
figure;
hold on;
plot(r,a)
plot(r,b)
legend("ML bound on |I(R)|", "|I(R)|")
hold off;