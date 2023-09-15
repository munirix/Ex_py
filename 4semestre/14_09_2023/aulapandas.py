# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import os
from datetime import date

Qfcst = pd.read_csv('Qglofas_PORTOVELHO_20230913.csv')

Qfcst['datetime']=pd.to_datetime(["{dt:%F}".format(dt=i) for i in
                              pd.date_range(date(2023,9,13),periods=len(Qfcst))])
Qfcst.set_index('datetime', inplace=True)

Qfcst_mean=Qfcst.mean(axis=1)
Qfcst_Q75=Qfcst.quantile(axis=1, q=0.75)
Qfcst_Q25=Qfcst.quantile(axis=1, q=0.25)
Qfcst_stdp=Qfcst_mean + Qfcst.std(axis=1)
Qfcst_stdm=Qfcst_mean - Qfcst.std(axis=1)

ax = Qfcst.plot(color='cyan',legend=False)
Qfcst_stdm.plot(ax=ax,color='red')
Qfcst_stdp.plot(ax=ax,color='red')
Qfcst_Q25.plot(ax=ax,color='yellow')
Qfcst_Q75.plot(ax=ax,color='yellow')
Qfcst_mean.plot(ax=ax,color='blue')
