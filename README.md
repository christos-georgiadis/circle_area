# circle_area
Approximating circle's area with rectangulars

\documentclass[tikz,border=5]{standalone}
\tikzset{declare function={y(\x)=4-\x^2;},
  plot fill/.style={fill=purple!75},
  plot/.style={draw=black!80, thick},
  bar/.style={fill=cyan, draw=white, thick},
  marking/.style={fill=cyan!50!black, draw=cyan!50!black},
  axis/.style={thick, draw=black!65, stealth-stealth}
}
\begin{document}
\begin{tikzpicture}[x=1.5cm, line cap=round, line join=round] 
\foreach \k [count=\z] in {0, 1/4, 1/2}{
\begin{scope}[shift=(0:\z*3)]
\path [plot fill] plot [domain=0:2] (\x,{y(\x)}) -| cycle;
\foreach \x in {0, 1/2, 1, 3/2}
   \path [bar]  (\x,0) |- (\x+1/2, {y(\x+\k)}) |- cycle;
\path [plot]  plot [domain=0:2] (\x,{y(\x)});
\path [axis] (0,4.5) |- (2.5,0);
\foreach \t [count=\x from 0] in {0,\frac{1}{2},1,\frac{3}{2},2}
  \path [axis, -] (\x/2,0) -- ++(0,-3pt) node [below] {$\t$};
\foreach \y in {0,4}
  \path [axis, -] (0,\y) -- ++(-3pt, 0) node [left] {$\y$};
\foreach \x in {0, 1/2, 1, 3/2}
   \path [marking]  (\x+\k, {y(\x+\k)}) circle [radius=1.5pt];
\end{scope}
}
\end{tikzpicture}
\end{document}
