"""
code: ic_cotainers.py
description: namedtuples describing miscellaenous containers to
pass info around.

credits: see ic_authors_and_legal.rst in /doc

last revised: JJGC, 10-July-2017
"""

import sys

from collections import namedtuple


this_module = sys.modules[__name__]

def _add_namedtuple_in_this_module(name, attribute_names):
    new_nametuple = namedtuple(name, attribute_names)
    setattr(this_module, name, new_nametuple)

for name, attrs in (
        ('DataVectors'    , 'pmt sipm mc events trg_type trg_channels'),
        ('SensorData'     , 'NPMT PMTWL NSIPM SIPMWL '),
        ('PmapVectors'    , 'pmaps events timestamps mc'),
        ('RawVectors'     , 'event pmtrwf sipmrwf pmt_active sipm_active'),
        ('CalibParams'    , 'coeff_c coeff_blr adc_to_pes_pmt adc_to_pes_sipm'),
        ('DeconvParams'   , 'n_baseline thr_trigger'),
        ('CalibVectors'   , 'channel_id coeff_blr coeff_c adc_to_pes adc_to_pes_sipm pmt_active'),
        ('S12Params'      , 'time stride length rebin_stride'),
        ('PmapParams'     , 's1_params s2_params s1p_params s1_PMT_params s1p_PMT_params'),
        ('ThresholdParams', 'thr_s1 thr_s2 thr_MAU thr_sipm thr_SIPM'),
        ('CSum'           , 'csum csum_mau'),
        ('CCWf'           , 'ccwf ccwf_mau'),
        ('S12Sum'         , 's1_ene s1_indx s2_ene s2_indx'),
        ('ZsWf'           , 'indices energies'),
        ('CalibratedPMT'  , 'CPMT CPMT_mau'),
        ('S1PMaps'        , 'S1 S1_PMT S1p S1p_PMT'),
        ('PMaps'          , 'S1 S2 S2Si'),
        ('Peak'           , 't E'),
        ('FitFunction'    , 'fn values errors chi2 pvalue cov'),
        ('TriggerParams'  , 'trigger_channels min_number_channels charge height width'),
        ('PeakData'       , 'charge height width'),
        ('Measurement'    , 'value uncertainty')):
    _add_namedtuple_in_this_module(name, attrs)

# Leave nothing but the namedtuple types in the namespace of this module
del name, namedtuple, sys, this_module, _add_namedtuple_in_this_module
