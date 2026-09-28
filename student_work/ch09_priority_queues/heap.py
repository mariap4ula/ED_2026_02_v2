class Heap:
    def __init__(self):
        self.arreglo = [float('-inf')]

    def insert(self, valor):
        self.arreglo.append(valor)
        i = len(self.arreglo) - 1
        while i > 1 and self.arreglo[i // 2] > self.arreglo[i]:
            self.arreglo[i // 2], self.arreglo[i] = self.arreglo[i], self.arreglo[i // 2]
            i = i // 2

    def remove_smallest(self):
        if len(self.arreglo) <= 1:
            return None
        if len(self.arreglo) == 2:
            return self.arreglo.pop()

        minimo = self.arreglo[1]
        self.arreglo[1] = self.arreglo.pop()

        i = 1
        while 2 * i < len(self.arreglo):
            hijo_izq = 2 * i
            hijo_der = 2 * i + 1
            menor = i

            if self.arreglo[hijo_izq] < self.arreglo[menor]:
                menor = hijo_izq

            if hijo_der < len(self.arreglo) and self.arreglo[hijo_der] < self.arreglo[menor]:
                menor = hijo_der

            if menor != i:
                self.arreglo[i], self.arreglo[menor] = self.arreglo[menor], self.arreglo[i]
                i = menor
            else:
                break

        return minimo

    def build_heap(self, lista):
        self.arreglo = [float('-inf')] + list(lista)
        for i in range(len(self.arreglo) - 1, 0, -1):
            self._bubble_down(i)

    def _bubble_down(self, i):
        while 2 * i < len(self.arreglo):
            hijo_izq = 2 * i
            hijo_der = 2 * i + 1
            menor = i

            if self.arreglo[hijo_izq] < self.arreglo[menor]:
                menor = hijo_izq

            if hijo_der < len(self.arreglo) and self.arreglo[hijo_der] < self.arreglo[menor]:
                menor = hijo_der

            if menor != i:
                self.arreglo[i], self.arreglo[menor] = self.arreglo[menor], self.arreglo[i]
                i = menor
            else:
                break
