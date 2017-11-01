#!/usr/bin/python
# -*- coding: utf-8 -*-

precio = 30
articulos = 6


if articulos >= 5:
    print("Tienes descuento")
    descuento = (precio*articulos)*.95
    print("Tienes que pagar", int(descuento))
else:
    print("No tienes descuento")
