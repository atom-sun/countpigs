(* Mathematica Source File *)
(* Created by the Wolfram Language Plugin for IntelliJ, see http://wlplugin.halirutan.de/ *)

(* :Title: CountPigs analytical solution: recursion formula *)
(* :Author: Ning Sun *)
(* :Date: 2019-11-04 *)
(* :Copyright: (c) 2019 atom-sun *)
(* :Mathematica Version: 12.0 *)

f[m_, q_, k_] := Sum[Binomial[k-j, q-j] * Binomial[k, j] * f[m-1, q, k-j],
  {j, 0, q}];
f[m_, q_, k_] := 0 /; k < q;
f[m_, q_, k_] := 1 /; k == q;
f[m_, q_, k_] := 0 /; m * q < k;
p[n_, m_, q_, k_] := Binomial[n, k] * f[m, q, k] / Binomial[n, q] ^ m;
(* Todo: add cache utility *)


(* :Examples: *)
(* Counting factors *)
Print[f[5, 1, 3]];
Print[f[5, 2, 3]];
Print[f[10, 3, 7]];

(* Probability *)
Print[p[5,3,1,2]];
Print[p[5,3,2,3]];
Print[p[4,3,1,1] + p[4,3,1,2] + p[4,3,1,3]];

(* Expectation value of k *)
ev[n_, m_, q_] := Sum[p[n, m, q, k] * k, {k, 0, m * q}];
Print[ev[4, 3, 1]];
Print[ev[10, 5, 3]];
Print[ev[15, 7, 3]];
Print[ev[20, 10, 3]];


(* Numerical timing *)
pn[n_, m_, q_, k_] := N[Binomial[n, k] * N[f[m, q, k]] / Binomial[n, q] ^ m];
evn[n_, m_, q_] := Sum[N[pn[n, m, q, k] * k], {k, 0, m * q}];
Print[evn[4, 3, 1]];
Print[evn[10, 5, 3]];
Print[evn[15, 7, 3]];
Print[evn[20, 10, 3]];
