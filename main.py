import numpy as np
import random
import math
import matplotlib.pyplot as plt


def main():

    mab = (a + b) / 2
    aa = np.array([0.05 * mab + 0.3 * mab * random.random() for _ in range(Nb)])
    bb = np.array([0.05 * mab + 0.3 * mab * random.random() for _ in range(Nb)])

    m2 = min(np.concatenate((aa, bb))) / 2
    AA = np.multiply(aa, bb)

    penalty = 0.2 * a * b
    nac = 0.8
    N = 500
    ng = 1500
    pmpe = 0.05
    pmbj = 0.01
    pmsj = 0.02
    pmrr = 0.05
    pmvi = 0.05
    pmne = 0.01

    G = np.zeros((N, 4, Nb))

    plt.figure()

    for Nc in range(N):
        for Nbc in range(Nb):
            G[Nc, 0, Nbc] = math.ceil(0.2 - random.random())
            G[Nc, 1, Nbc] = math.ceil(0.5 - random.random())
            G[Nc, 2, Nbc] = m2 + (a - m2) * random.random()
            G[Nc, 3, Nbc] = m2 + (b - m2) * random.random()

    for ngc in range(ng):
        fitnesses = np.zeros(N)

        for Nc in range(N):
            G1 = G[Nc, :, :].copy()
            ind = np.nonzero(G1[0, :])[0]
            L = len(ind)
            fitness = 0
            ispen = False

            if L > 0:
                rot = [G1[1, index] for index in ind]
                x = [G1[2, index] for index in ind]
                y = [G1[3, index] for index in ind]

                for n in range(L):
                    ind1 = ind[n]

                    aaa = aa[ind1]
                    bbb = bb[ind1]
                    A0 = AA[ind1]

                    if rot[n]:
                        aaa, bbb = bbb, aaa

                    x1 = max(x[n] - aaa / 2, 0)
                    y1 = max(y[n] - bbb / 2, 0)
                    x2 = min(x[n] + aaa / 2, a)
                    y2 = min(y[n] + bbb / 2, b)

                    if (x1 >= x2) or (y1 >= y2):
                        A = 0
                    else:
                        A = (x2 - x1) * (y2 - y1)

                    if (aaa / 2 <= x[n]) and (x[n] <= a - aaa / 2) and (bbb / 2 <= y[n]) and (y[n] <= b - bbb / 2):
                        fitness = fitness + A
                    else:
                        fitness = fitness + A - nac * (A0 - A)
                        ispen = True

                for n1 in range(L - 1):
                    ind1 = ind[n1]
                    aaa1 = aa[ind1]
                    bbb1 = bb[ind1]
                    x1 = x[n1]
                    y1 = y[n1]

                    if rot[n1]:
                        aaa1, bbb1 = bbb1, aaa1

                    for n2 in range(n1 + 1, L):
                        ind2 = ind[n2]
                        aaa2 = aa[ind2]
                        bbb2 = bb[ind2]
                        x2 = x[n2]
                        y2 = y[n2]

                        if rot[n2]:
                            aaa2, bbb2 = bbb2, aaa2

                        dx = abs(x1 - x2)
                        dy = abs(y1 - y2)
                        a12 = (aaa1 + aaa2) / 2
                        b12 = (bbb1 + bbb2) / 2

                        if (dx < a12) and (dy < b12):
                            ispen = True
                            Ac = (a12 - dx) * (b12 - dy)
                            fitness = fitness - 2 * Ac - 2 * nac * Ac

            if ispen:
                fitness = fitness - penalty

            fitnesses[Nc] = fitness

        best = np.argmax(fitnesses)
        Gb = G[best, :].copy()
        # print(Gb)  # ------plot this------ #

        if ngc % 10 == 0:
            plt.clf()
            plt.title('Current generation: ' + str(ngc))
            plt.plot([0, a, a, 0, 0], [0, 0, b, b, 0], 'b-')
            plt.xlim([-0.1 * a, 1.1 * a])
            plt.ylim([-0.1 * b, 1.1 * b])

            for Nbc in range(Nb):
                if Gb[0, Nbc]:
                    aaa = aa[Nbc]
                    bbb = bb[Nbc]
                    if Gb[1, Nbc]:
                        aaa, bbb = bbb, aaa

                    x = Gb[2, Nbc]
                    y = Gb[3, Nbc]
                    plt.plot([x - aaa / 2, x + aaa / 2, x + aaa / 2, x - aaa / 2, x - aaa / 2],
                             [y - bbb / 2, y - bbb / 2, y + bbb / 2, y + bbb / 2, y - bbb / 2], '-')

            plt.draw()
            plt.pause(0.05)

        fmn = min(fitnesses)
        fst = max(float(np.std(fitnesses)), 1E-7)
        fmn1 = fmn - 0.01 * fst
        P = fitnesses - fmn1
        p = P / sum(P)
        ii = random.choices(population=np.arange(len(p)), weights=p, k=N)
        Gch = np.zeros((N, 4, Nb))

        for n in range(0, N, 2):
            Gpr1 = G[ii[n], :].copy()
            Gpr2 = G[ii[n + 1], :].copy()

            Gch1 = np.zeros((4, Nb))
            Gch2 = np.zeros((4, Nb))

            for Nbc in range(Nb):
                if random.random() < 0.5:
                    Gch1[0, Nbc] = Gpr1[0, Nbc]
                else:
                    Gch1[0, Nbc] = Gpr2[0, Nbc]

                if random.random() < 0.5:
                    Gch2[0, Nbc] = Gpr1[0, Nbc]
                else:
                    Gch2[0, Nbc] = Gpr2[0, Nbc]

                if random.random() < 0.5:
                    Gch1[1, Nbc] = Gpr1[1, Nbc]
                else:
                    Gch1[1, Nbc] = Gpr2[1, Nbc]

                if random.random() < 0.5:
                    Gch2[1, Nbc] = Gpr1[1, Nbc]
                else:
                    Gch2[1, Nbc] = Gpr2[1, Nbc]

                i3 = math.floor(random.uniform(0, 3))
                if i3 == 0:
                    Gch1[2, Nbc] = (Gpr1[2, Nbc] + Gpr2[2, Nbc]) / 2
                    Gch1[3, Nbc] = (Gpr1[3, Nbc] + Gpr2[3, Nbc]) / 2
                elif i3 == 1:
                    Gch1[2, Nbc] = Gpr1[2, Nbc]
                    Gch1[3, Nbc] = Gpr1[3, Nbc]
                else:
                    Gch1[2, Nbc] = Gpr2[2, Nbc]
                    Gch1[3, Nbc] = Gpr2[3, Nbc]

                i3 = math.floor(random.uniform(0, 3))
                if i3 == 0:
                    Gch2[2, Nbc] = (Gpr1[2, Nbc] + Gpr2[2, Nbc]) / 2
                    Gch2[3, Nbc] = (Gpr1[3, Nbc] + Gpr2[3, Nbc]) / 2
                elif i3 == 1:
                    Gch2[2, Nbc] = Gpr1[2, Nbc]
                    Gch2[3, Nbc] = Gpr1[3, Nbc]
                else:
                    Gch2[2, Nbc] = Gpr2[2, Nbc]
                    Gch2[3, Nbc] = Gpr2[3, Nbc]

            Gch[n, :] = Gch1.copy()
            Gch[n + 1, :] = Gch2.copy()

        G = Gch.copy()

        for Nc in range(N):
            if random.random() < pmpe:
                ir1 = math.floor(Nb * random.random())
                ir2 = math.floor(Nb * random.random())
                G[Nc, 2, ir1], G[Nc, 2, ir2] = G[Nc, 2, ir2], G[Nc, 2, ir1]
                G[Nc, 3, ir1], G[Nc, 3, ir2] = G[Nc, 3, ir2], G[Nc, 3, ir1]

        for Nc in range(N):
            if random.random() < pmbj:
                ir = math.floor(Nb * random.random())
                G[Nc, 2, ir] = G[Nc, 2, ir] + 0.05 * a * random.normalvariate(0, 1)
                G[Nc, 3, ir] = G[Nc, 3, ir] + 0.05 * b * random.normalvariate(0, 1)

        for Nc in range(N):
            if random.random() < pmsj:
                ir = math.floor(Nb * random.random())
                G[Nc, 2, ir] = G[Nc, 2, ir] + 0.005 * a * random.normalvariate(0, 1)
                G[Nc, 3, ir] = G[Nc, 3, ir] + 0.005 * b * random.normalvariate(0, 1)

        for Nc in range(N):
            if random.random() < pmrr:
                ir = math.floor(Nb * random.random())
                G[Nc, 1, ir] = math.ceil(0.5 - random.random())

        for Nc in range(N):
            if random.random() < pmvi:
                ir = math.floor(Nb * random.random())
                G[Nc, 0, ir] = math.ceil(0.5 - random.random())

        for Nc in range(N):
            if random.random() < pmne:
                ir = math.floor(Nb * random.random())

                rv = np.nonzero(G[Nc, 0, :])[0]
                rv = rv[rv != Nc]

                if random.random() < 0.5:
                    eax1 = [G[Nc, 2, rvc] - aa[rvc] / 2 for rvc in rv]
                    eax2 = [G[Nc, 2, rvc] + aa[rvc] / 2 for rvc in rv]
                    eax = np.concatenate((eax1, eax2, [0, a]))

                    deax1 = G[Nc, 2, ir] - aa[ir] / 2 - eax
                    deax2 = G[Nc, 2, ir] + aa[ir] / 2 - eax
                    deax = np.concatenate((deax1, deax2))

                    indm = np.argmin(abs(deax))
                    G[Nc, 2, ir] = G[Nc, 2, ir] - deax[indm]

                else:
                    eay1 = [G[Nc, 3, rvc] - bb[rvc] / 2 for rvc in rv]
                    eay2 = [G[Nc, 3, rvc] + bb[rvc] / 2 for rvc in rv]
                    eay = np.concatenate((eay1, eay2, [0, b]))

                    deay1 = G[Nc, 3, ir] - bb[ir] / 2 - eay
                    deay2 = G[Nc, 3, ir] + bb[ir] / 2 - eay
                    deay = np.concatenate((deay1, deay2))

                    indm = np.argmin(abs(deay))
                    G[Nc, 3, ir] = G[Nc, 3, ir] - deay[indm]

        G[0, :] = Gb.copy()
        random.shuffle(G)


if __name__ == "__main__":
    main()
