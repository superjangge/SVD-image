# SVD壓縮圖片

SVD圖片壓縮主要是利用 [low rank approximation](https://en.wikipedia.org/wiki/Low-rank_approximation) 來做圖片壓縮。 選定 $d\leq \min \{w,h \}$，其中 w,h 是圖的寬與高。 接著會取出 $U_d$, $\Sigma_d$, $V_d$，它們分別是  $h\times d$ 矩陣、 $d\times d$ 對角矩陣、 $ d\times w$ 矩陣。      
