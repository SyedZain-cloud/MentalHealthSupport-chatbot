# Five-seed paired RAMHA–MERCURY experiment

Seeds: [17, 42, 73, 101, 303]

| Split | RAMHA macro-F1 mean±SD | MERCURY macro-F1 mean±SD | Mean Δ | Exact sign-flip p |
|---|---:|---:|---:|---:|
| test | 0.927380 ± 0.010315 | 0.929981 ± 0.009760 | +0.002601 | 0.0625 |
| test_balanced | 0.925094 ± 0.008556 | 0.925064 ± 0.009706 | -0.000029 | 0.8750 |
| test_masked | 0.878510 ± 0.016461 | 0.885669 ± 0.011001 | +0.007159 | 0.0625 |

Inference must account for the small sample of five seeds. The exact two-sided sign-flip test has a minimum attainable p-value of 0.0625.