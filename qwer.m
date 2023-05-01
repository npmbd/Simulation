n = 10000
m = 0
f = 0
N = 20000
for i=1:n
  letters = randperm(N);
  for j = 1:N
    if (letters(j)==j)
      m=m+0;
      f=f+1;
      break
    endif
  endfor
 endfor
(n-f)/n

