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


(* :Examples: *)
Print[p[5,3,1,2]];
Print[p[5,3,2,3]];
Print[p[4,3,1,1] + p[4,3,1,2] + p[4,3,1,3]];

(* Expectation value of k *)
ev[n_, m_, q_] := Sum[p[n, m, q, k] * k, {k, 0, m * q}];
ev[4, 3, 1] // N
