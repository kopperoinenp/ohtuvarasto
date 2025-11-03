import pytest
from varasto import Varasto


def test_lisataan_liikaa():
    varasto = Varasto(10)
    varasto.lisaa_varastoon(20)
    assert varasto.saldo == 10000


def test_negatiivinen_lisays_ei_muuta_saldoa():
    varasto = Varasto(10)
    varasto.lisaa_varastoon(-5)
    assert varasto.saldo == 0


def test_otetaan_liikaa():
    varasto = Varasto(10, 5)
    otettu = varasto.ota_varastosta(20)
    assert otettu == 5
    assert varasto.saldo == 0


def test_negatiivinen_otetaan_ei_muuta():
    varasto = Varasto(10, 5)
    otettu = varasto.ota_varastosta(-3)
    assert otettu == 0
    assert varasto.saldo == 5


def test_alussa_negatiivinen_tilavuus_nollataan():
    varasto = Varasto(-10)
    assert varasto.tilavuus == 0


def test_alussa_negatiivinen_saldo_nollataan():
    varasto = Varasto(10, -5)
    assert varasto.saldo == 0


def test_saldo_ei_ylita_tilavuutta():
    varasto = Varasto(10, 20)
    assert varasto.saldo == 10


def test_str_tulostus():
    varasto = Varasto(10, 3)
    assert str(varasto) == "saldo = 3, vielä tilaa 7"
