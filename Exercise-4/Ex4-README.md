# Analysis of Information Networks

## Exercise 4: Disease Spread

### Problem Statement:
- **Task**: In the Zachary Club network, compute the characteristic time $t$ and the epidemic threshold $\lambda$ for the SI, SIS, and SIR models. The value of $\beta$ can be selected from a suitable reference article (as exemplified below). Before use, slightly randomize $\beta$ to ensure varied results across different groups.

### Reference Article:
Kolokolnikov, T. and Iron, D. (2021). “Law of mass action and saturation in SIR model with application to Coronavirus modelling.” *Infectious Disease Modelling*, 6, pp. 91–97. Available at: [https://doi.org/10.1016/j.idm.2020.11.002](https://doi.org/10.1016/j.idm.2020.11.002).

### Objectives:
1. **Calculate the average degree** $\langle k \rangle$ of the network.
2. **Compute** $\langle k^2 \rangle$.
3. **Determine the characteristic time** $T_{SI}$, $T_{SIS}$, and $T_{SIR}$ for the given models.
4. **Calculate the epidemic thresholds** $\lambda$, $\lambda_{c_{SIS}}$, and $\lambda_{c_{SIR}}$.

### Steps:
1. **Read the Zachary dataset**: Load the network data from a file.
2. **Compute the degrees of the nodes** and calculate the average degree.
3. **Collect user inputs** for the parameters $\beta$ and $\mu$.
4. **Perform calculations** for $T_{SI}$, $T_{SIS}$, and $T_{SIR}$ using the following formulas:
   - $T_{SI} = \frac{\langle k \rangle}{\beta \cdot (\langle k^2 \rangle - \langle k \rangle)}$
   - $T_{SIS} = \frac{\langle k \rangle}{\beta \cdot \langle k^2 \rangle - \mu \cdot \langle k \rangle}$
   - $T_{SIR} = \frac{\langle k \rangle}{\beta \cdot \langle k^2 \rangle - (\mu + \beta) \cdot \langle k \rangle}$
5. **Calculate the epidemic thresholds**:
   - $\lambda = \frac{\beta}{\mu}$
   - $\lambda_{c_{SIS}} = \frac{\langle k \rangle}{\langle k^2 \rangle}$
   - $\lambda_{c_{SIR}} = \frac{1}{\frac{\langle k^2 \rangle}{\langle k \rangle} - 1}$

### Outputs:
- **Average Degree** $\langle k \rangle$
- **Second Moment** $\langle k^2 \rangle$
- **Characteristic Times** $T_{SI}$, $T_{SIS}$, $T_{SIR}$
- **Epidemic Thresholds** $\lambda$, $\lambda_{c_{SIS}}$, $\lambda_{c_{SIR}}$

### References:
The Zachary Club Network dataset is a widely used social network dataset that models relationships among members of a karate club.
