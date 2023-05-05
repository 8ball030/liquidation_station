# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2023 zarathustra
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""This module contains the contract packages."""

from dataclasses import dataclass


@dataclass
class OVIX_CONTRACT_ADDRESSES_POLYGON_POS:
    COMPTROLLER = "0xf29d0ae1A29C453df338C5eEE4f010CFe08bb3FF"
    UNITROLLER = "0x8849f1a0cB6b5D6076aB150546EddEe193754F1C"
    ORACLE = "0x421FF03Fe1085bce50ec5Bf06c5907119d87672F"
    JUMP_INTEREST_MODEL = "0x15c7DAaD15E3EE00C30C16D6294ea3528641165a"

    # Tokens
    O_MATIC_LOGIC = "0x188D24cfEB2837c11Fd22F1462C6E0174cD910Bc"
    O_MATIC = "0xE554E874c9c60E45F1Debd479389C76230ae25A8"
    O_TOKEN_LOGIC = "0xb329FC9379dBf71BC58178383BA494D10D4E296F"
    O_WBTC = "0x3B9128Ddd834cE06A60B0eC31CCfB11582d8ee18"
    O_DAI = "0x2175110F2936bf630a278660E9B6E4EFa358490A"
    O_WETH = "0xb2D9646A1394bf784E376612136B3686e74A325F"
    O_USDC = "0xEBb865Bf286e6eA8aBf5ac97e1b56A76530F3fBe"
    O_USDT = "0x1372c34acC14F1E8644C72Dad82E3a21C211729f"
    O_MAI = "0xC57E5e261d49Af3026446de3eC381172f17bB799"
    O_MATICX = "0xAAcc5108419Ae55Bc3588E759E28016d06ce5F40"

    # NOTE: Contract source code not verified
    OJ_EUR = "0x29b0F07d5A61595685a17D5F9F86313742Ebd6Bc"
    O_GDAI = "0x6F063Fe661d922e4fd77227f8579Cb84f9f41F0B"
    OV_GHST = "0xE053A4014b50666ED388ab8CbB18D5834de0aB12"
    OWST_ETH = "0xf06eda703c62b9889c75dccde927b93bde1ae654"
    MAXIMILLION = "0x3eA022fA3606fffF3eD522a87Bf45965F2dDD236"
