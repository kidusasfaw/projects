declare
type sims IS VARRAY(1000) of number;
results sims;
nsim number;
start_pos number;
stop_pos number;
init_pos number;
position number;
prob_right number;
rand number;
zeros number;
ones number;
begin
results := sims();
nsim := 1000;
start_pos := 0;
stop_pos := 1;
init_pos := 0.5;
prob_right := 0.7;
zeros := 0;
ones := 0;
for i in 1 .. nsim
loop
position := init_pos;
WHILE (position <> start_pos and position <> stop_pos)
LOOP
   select round(dbms_random.value) into rand from dual;
   if rand > prob_right then
   position := position + 0.1;
   else
   position := position - 0.1;
   end if;
END LOOP;
results.extend;
results(i) := position;
end loop;
for i in 1 .. nsim
loop
if results(i) = 0 then
   zeros := zeros + 1;
   else
   ones := ones + 1;
end if;
end loop;
dbms_output.put_line('Zeros '||zeros);
dbms_output.put_line('Ones '||ones);
end;
/