% Henry A. Boateng
% April 04, 2022
% This program provides an example of truncation and round-off error 
% using a forward difference approximation. 

% Define the function to be differentiated and its derivative
f = @(x) exp(x);  fp = @(x) exp(x);
%f = @(x) 1+x+x.^3; fp = @(x) 1+3*x.^2;

% The point where the derivative is needed;
x = 1;
exact_deriv_value = fp(x);

% The discretization sizes
h=0.1./2.^(0:1:65);

% Find the forward difference approximation to the derivative f'(x) for
% different h values
fpappx = fwd_diff(f,x,h);
error  = exact_deriv_value - fpappx;
abserror = abs(error);
eh  = error./h;
eh2 = error./h.^2;

fprintf('%8s \t\t %10s \t\t\t %12s \t\t\t %12s\n','h', 'error', 'error/h', 'error/h^2')
for i=1:length(h)
    fprintf('%12.8e\t\t %12.8e\t\t %12.8e \t\t %12.8e\n',h(i),error(i),eh(i),eh2(i))
end


loglog(h,abserror,'o-','LineWidth',2,'MarkerSize',6);
xlabel('h (step size)');ylabel('error')
%saveas(1,'fwdDiff_error_plot.png')

function [fp]= fwd_diff(f,x,h)
    % Forward difference approximation for the first derivative
    % Inputs
    % f  - the function to be differentiated
    % x  - the point where the derivative is needed
    % h  - the step/discretization size
    % Output
    % fp - f'(x)

    fp = (f(x+h) - f(x))./h;
end

