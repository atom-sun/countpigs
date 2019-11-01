(* :Mathematica Version: 12.0 *)
(* :Copyright: (c) 2019 atom-sun *)

(* :Title: CountPigs *)
(* :Author: Ning Sun *)
(* :Date: 2019-11-01 *)

directCountPigs[n_, m_, q_, k_] :=
    Module[{zhujuan, choice, choices, x0, x1},
      zhujuan = Array[Subscript[pig, #]&, n];
      choice = DeleteDuplicates[Sort/@Select[Tuples[zhujuan, q],
            DuplicateFreeQ]];
      choices= Tuples[choice, m];
      x0 = Length[choices];
      x1 = Count[Length/@Tally/@Flatten/@choices, k];
      x1/x0
    ];

(* :Usage: *)
Print[directCountPigs[5,3,1,2]];
Print[directCountPigs[5,3,2,3]];
