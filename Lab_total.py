#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Lab Total
# Generated: Fri Mar  1 12:16:28 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from b_Eye_Diagram_simple_c import b_Eye_Diagram_simple_c  # grc-generated hier_block
from b_Mod_BPSK_bc import b_Mod_BPSK_bc  # grc-generated hier_block
from b_sampler_cc import b_sampler_cc  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import cmath
import math
import numpy
import random
import sip
import wform  # embedded python module
from gnuradio import qtgui


class Lab_total(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Lab Total")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Lab Total")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "Lab_total")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.m = m = 9
        self.samp_rate_usrp = samp_rate_usrp = 100000000
        self.Kd = Kd = math.pow(2,m)
        self.Constelacion = Constelacion = [1.+0.j,    -1.+0.j ]
        self.samp_rate = samp_rate = int(samp_rate_usrp/Kd)
        self.Sps = Sps = 16
        self.M = M = len(Constelacion)
        self.rolloff = rolloff = 0.35
        self.ntaps = ntaps = 128
        self.Rs = Rs = samp_rate/Sps
        self.Bps = Bps = int(math.log(M,2))
        self.run_stop = run_stop = True
        self.hrrc = hrrc = wform.rrcos(Sps,ntaps,rolloff)
        self.hrc = hrc = wform.rcos(Sps,ntaps,rolloff)
        self.hr = hr = wform.rect(Sps,ntaps)
        self.hn = hn = wform.nyq(Sps,ntaps)
        self.Tmax_scope = Tmax_scope = 64./Rs
        self.TimingDelay = TimingDelay = 0
        self.Rb = Rb = Rs*Bps
        self.NodB = NodB = -65

        self.MiconstellationObject = MiconstellationObject = digital.constellation_calcdist((Constelacion), (), 4, 1).base()

        self.Fc = Fc = 80e6
        self.BW = BW = samp_rate/2.

        ##################################################
        # Blocks
        ##################################################
        self.pestana = Qt.QTabWidget()
        self.pestana_widget_0 = Qt.QWidget()
        self.pestana_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_0)
        self.pestana_grid_layout_0 = Qt.QGridLayout()
        self.pestana_layout_0.addLayout(self.pestana_grid_layout_0)
        self.pestana.addTab(self.pestana_widget_0, 'Osciloscopio Wave Forming')
        self.pestana_widget_1 = Qt.QWidget()
        self.pestana_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_1)
        self.pestana_grid_layout_1 = Qt.QGridLayout()
        self.pestana_layout_1.addLayout(self.pestana_grid_layout_1)
        self.pestana.addTab(self.pestana_widget_1, 'PSD Wave Forming')
        self.pestana_widget_2 = Qt.QWidget()
        self.pestana_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_2)
        self.pestana_grid_layout_2 = Qt.QGridLayout()
        self.pestana_layout_2.addLayout(self.pestana_grid_layout_2)
        self.pestana.addTab(self.pestana_widget_2, 'Osciloscopio Acoplamiento')
        self.pestana_widget_3 = Qt.QWidget()
        self.pestana_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_3)
        self.pestana_grid_layout_3 = Qt.QGridLayout()
        self.pestana_layout_3.addLayout(self.pestana_grid_layout_3)
        self.pestana.addTab(self.pestana_widget_3, 'PSD Acoplamiento')
        self.pestana_widget_4 = Qt.QWidget()
        self.pestana_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.pestana_widget_4)
        self.pestana_grid_layout_4 = Qt.QGridLayout()
        self.pestana_layout_4.addLayout(self.pestana_grid_layout_4)
        self.pestana.addTab(self.pestana_widget_4, 'Diagrama de Ojo')
        self.top_grid_layout.addWidget(self.pestana, 1, 0, 1, 4)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.ojo = Qt.QTabWidget()
        self.ojo_widget_0 = Qt.QWidget()
        self.ojo_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.ojo_widget_0)
        self.ojo_grid_layout_0 = Qt.QGridLayout()
        self.ojo_layout_0.addLayout(self.ojo_grid_layout_0)
        self.ojo.addTab(self.ojo_widget_0, 'Rectangular')
        self.ojo_widget_1 = Qt.QWidget()
        self.ojo_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.ojo_widget_1)
        self.ojo_grid_layout_1 = Qt.QGridLayout()
        self.ojo_layout_1.addLayout(self.ojo_grid_layout_1)
        self.ojo.addTab(self.ojo_widget_1, 'Nyquist')
        self.ojo_widget_2 = Qt.QWidget()
        self.ojo_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.ojo_widget_2)
        self.ojo_grid_layout_2 = Qt.QGridLayout()
        self.ojo_layout_2.addLayout(self.ojo_grid_layout_2)
        self.ojo.addTab(self.ojo_widget_2, 'Raised Cosine')
        self.ojo_widget_3 = Qt.QWidget()
        self.ojo_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.ojo_widget_3)
        self.ojo_grid_layout_3 = Qt.QGridLayout()
        self.ojo_layout_3.addLayout(self.ojo_grid_layout_3)
        self.ojo.addTab(self.ojo_widget_3, 'Root Raised Cosine')
        self.pestana_grid_layout_4.addWidget(self.ojo)
        self._TimingDelay_range = Range(0, Sps-1, 1, 0, 200)
        self._TimingDelay_win = RangeWidget(self._TimingDelay_range, self.set_TimingDelay, 'Timing', "counter_slider", int)
        self.top_grid_layout.addWidget(self._TimingDelay_win, 0, 3, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        _run_stop_check_box = Qt.QCheckBox('Inicial/Parar')
        self._run_stop_choices = {True: True, False: False}
        self._run_stop_choices_inv = dict((v,k) for k,v in self._run_stop_choices.iteritems())
        self._run_stop_callback = lambda i: Qt.QMetaObject.invokeMethod(_run_stop_check_box, "setChecked", Qt.Q_ARG("bool", self._run_stop_choices_inv[i]))
        self._run_stop_callback(self.run_stop)
        _run_stop_check_box.stateChanged.connect(lambda i: self.set_run_stop(self._run_stop_choices[bool(i)]))
        self.top_grid_layout.addWidget(_run_stop_check_box, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0_1 = qtgui.time_sink_c(
        	int(Tmax_scope*samp_rate)/4, #size
        	samp_rate, #samp_rate
        	"Wave Forming", #name
        	4 #number of inputs
        )
        self.qtgui_time_sink_x_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1.set_y_axis(-3, 3)

        self.qtgui_time_sink_x_0_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1.enable_control_panel(False)
        self.qtgui_time_sink_x_0_1.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_1.disable_legend()

        labels = ['Re', 'Im', 'Re.Nyq', 'Re.Nyq', 'Re.RC',
                  'Re.RC', 'Re.RRC', 'Re.RRC', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(8):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.pestana_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_1_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.pestana_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.pestana_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Wave Forming.PSD", #name
        	4 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-80, 10)
        self.qtgui_freq_sink_x_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(True)

        if not True:
          self.qtgui_freq_sink_x_0_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)

        labels = ['Rect', 'Nyq', 'RC', 'RRC', '',
                  '', '', '', '', '']
        widths = [3, 3, 3, 3, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(4):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.pestana_grid_layout_1.addWidget(self._qtgui_freq_sink_x_0_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.pestana_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.pestana_grid_layout_1.setColumnStretch(c, 1)
        self.interp_fir_filter_xxx_0_0_2 = filter.interp_fir_filter_ccc(1, (numpy.multiply(hrc,1./Sps)))
        self.interp_fir_filter_xxx_0_0_2.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0_0_1_0 = filter.interp_fir_filter_ccc(1, (numpy.multiply(hrrc,1./Sps)))
        self.interp_fir_filter_xxx_0_0_1_0.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0_0_1 = filter.interp_fir_filter_ccc(1, (numpy.multiply(hn,1./Sps)))
        self.interp_fir_filter_xxx_0_0_1.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0_0_0_0_1 = filter.interp_fir_filter_ccc(Sps, (hrrc))
        self.interp_fir_filter_xxx_0_0_0_0_1.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0_0_0_0_0 = filter.interp_fir_filter_ccc(Sps, (hrc))
        self.interp_fir_filter_xxx_0_0_0_0_0.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0_0_0_0 = filter.interp_fir_filter_ccc(Sps, (hn))
        self.interp_fir_filter_xxx_0_0_0_0.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0_0_0 = filter.interp_fir_filter_ccc(Sps, (hr))
        self.interp_fir_filter_xxx_0_0_0.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0_0 = filter.interp_fir_filter_ccc(1, (numpy.multiply(hr,1./Sps)))
        self.interp_fir_filter_xxx_0_0.declare_sample_delay(0)
        self.digital_constellation_decoder_cb_0_0 = digital.constellation_decoder_cb(MiconstellationObject)
        self.blocks_null_sink_0_0 = blocks.null_sink(gr.sizeof_char*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.b_sampler_cc_0_0 = b_sampler_cc(
            DelayDiez=TimingDelay,
            Sps=Sps,
        )
        self.b_Mod_BPSK_bc_0 = b_Mod_BPSK_bc()
        self.b_Eye_Diagram_simple_c_0_0_1 = b_Eye_Diagram_simple_c(
            AlphaLineas=0.5,
            Delay_i=0,
            GrosorLineas=20,
            Kint=1,
            N_eyes=2,
            Samprate1=samp_rate,
            Sps1=Sps,
            Title="Acoplamiento.RRC",
            Ymax=3,
            Ymin=-3,
        )
        self.ojo_grid_layout_3.addWidget(self.b_Eye_Diagram_simple_c_0_0_1)
        self.b_Eye_Diagram_simple_c_0_0_0 = b_Eye_Diagram_simple_c(
            AlphaLineas=0.5,
            Delay_i=0,
            GrosorLineas=20,
            Kint=1,
            N_eyes=2,
            Samprate1=samp_rate,
            Sps1=Sps,
            Title="Acoplamiento.RC",
            Ymax=3,
            Ymin=-3,
        )
        self.ojo_grid_layout_2.addWidget(self.b_Eye_Diagram_simple_c_0_0_0)
        self.b_Eye_Diagram_simple_c_0_0 = b_Eye_Diagram_simple_c(
            AlphaLineas=0.5,
            Delay_i=0,
            GrosorLineas=20,
            Kint=1,
            N_eyes=2,
            Samprate1=samp_rate,
            Sps1=Sps,
            Title="Acoplamiento.Nyq",
            Ymax=3,
            Ymin=-3,
        )
        self.ojo_grid_layout_1.addWidget(self.b_Eye_Diagram_simple_c_0_0)
        self.b_Eye_Diagram_simple_c_0 = b_Eye_Diagram_simple_c(
            AlphaLineas=0.5,
            Delay_i=0,
            GrosorLineas=20,
            Kint=1,
            N_eyes=2,
            Samprate1=samp_rate,
            Sps1=Sps,
            Title="Acoplamiento.Rect",
            Ymax=3,
            Ymin=-3,
        )
        self.ojo_grid_layout_0.addWidget(self.b_Eye_Diagram_simple_c_0)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 2, 1000)), True)
        self._NodB_range = Range(-140., 0., 1., -65, 200)
        self._NodB_win = RangeWidget(self._NodB_range, self.set_NodB, 'No (in dB for white noise)', "counter_slider", float)
        self.top_grid_layout.addWidget(self._NodB_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._BW_range = Range(0., samp_rate/2., (samp_rate/2)/128., samp_rate/2., 200)
        self._BW_win = RangeWidget(self._BW_range, self.set_BW, 'LPF BW (Hz)', "counter_slider", float)
        self.top_grid_layout.addWidget(self._BW_win, 0, 2, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.b_Mod_BPSK_bc_0, 0))
        self.connect((self.b_Mod_BPSK_bc_0, 0), (self.interp_fir_filter_xxx_0_0_0, 0))
        self.connect((self.b_Mod_BPSK_bc_0, 0), (self.interp_fir_filter_xxx_0_0_0_0, 0))
        self.connect((self.b_Mod_BPSK_bc_0, 0), (self.interp_fir_filter_xxx_0_0_0_0_0, 0))
        self.connect((self.b_Mod_BPSK_bc_0, 0), (self.interp_fir_filter_xxx_0_0_0_0_1, 0))
        self.connect((self.b_sampler_cc_0_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.b_sampler_cc_0_0, 1), (self.digital_constellation_decoder_cb_0_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0_0, 0), (self.blocks_null_sink_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.b_Eye_Diagram_simple_c_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.b_sampler_cc_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0_0, 0), (self.interp_fir_filter_xxx_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0_0, 0), (self.qtgui_freq_sink_x_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0_0, 0), (self.qtgui_time_sink_x_0_1, 0))
        self.connect((self.interp_fir_filter_xxx_0_0_0_0, 0), (self.interp_fir_filter_xxx_0_0_1, 0))
        self.connect((self.interp_fir_filter_xxx_0_0_0_0, 0), (self.qtgui_freq_sink_x_0_0, 1))
        self.connect((self.interp_fir_filter_xxx_0_0_0_0, 0), (self.qtgui_time_sink_x_0_1, 1))
        self.connect((self.interp_fir_filter_xxx_0_0_0_0_0, 0), (self.interp_fir_filter_xxx_0_0_2, 0))
        self.connect((self.interp_fir_filter_xxx_0_0_0_0_0, 0), (self.qtgui_freq_sink_x_0_0, 2))
        self.connect((self.interp_fir_filter_xxx_0_0_0_0_0, 0), (self.qtgui_time_sink_x_0_1, 2))
        self.connect((self.interp_fir_filter_xxx_0_0_0_0_1, 0), (self.interp_fir_filter_xxx_0_0_1_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0_0_0_1, 0), (self.qtgui_freq_sink_x_0_0, 3))
        self.connect((self.interp_fir_filter_xxx_0_0_0_0_1, 0), (self.qtgui_time_sink_x_0_1, 3))
        self.connect((self.interp_fir_filter_xxx_0_0_1, 0), (self.b_Eye_Diagram_simple_c_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0_1_0, 0), (self.b_Eye_Diagram_simple_c_0_0_1, 0))
        self.connect((self.interp_fir_filter_xxx_0_0_2, 0), (self.b_Eye_Diagram_simple_c_0_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Lab_total")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_m(self):
        return self.m

    def set_m(self, m):
        self.m = m
        self.set_Kd(math.pow(2,self.m))

    def get_samp_rate_usrp(self):
        return self.samp_rate_usrp

    def set_samp_rate_usrp(self, samp_rate_usrp):
        self.samp_rate_usrp = samp_rate_usrp
        self.set_samp_rate(int(self.samp_rate_usrp/self.Kd))

    def get_Kd(self):
        return self.Kd

    def set_Kd(self, Kd):
        self.Kd = Kd
        self.set_samp_rate(int(self.samp_rate_usrp/self.Kd))

    def get_Constelacion(self):
        return self.Constelacion

    def set_Constelacion(self, Constelacion):
        self.Constelacion = Constelacion
        self.set_M(len(self.Constelacion))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.b_Eye_Diagram_simple_c_0_0_1.set_Samprate1(self.samp_rate)
        self.b_Eye_Diagram_simple_c_0_0_0.set_Samprate1(self.samp_rate)
        self.b_Eye_Diagram_simple_c_0_0.set_Samprate1(self.samp_rate)
        self.b_Eye_Diagram_simple_c_0.set_Samprate1(self.samp_rate)
        self.set_Rs(self.samp_rate/self.Sps)
        self.set_BW(self.samp_rate/2.)

    def get_Sps(self):
        return self.Sps

    def set_Sps(self, Sps):
        self.Sps = Sps
        self.set_hrrc(wform.rrcos(self.Sps,self.ntaps,self.rolloff))
        self.set_hrc(wform.rcos(self.Sps,self.ntaps,self.rolloff))
        self.set_hr(wform.rect(self.Sps,self.ntaps))
        self.set_hn(wform.nyq(self.Sps,self.ntaps))
        self.interp_fir_filter_xxx_0_0_2.set_taps((numpy.multiply(self.hrc,1./self.Sps)))
        self.interp_fir_filter_xxx_0_0_1_0.set_taps((numpy.multiply(self.hrrc,1./self.Sps)))
        self.interp_fir_filter_xxx_0_0_1.set_taps((numpy.multiply(self.hn,1./self.Sps)))
        self.interp_fir_filter_xxx_0_0.set_taps((numpy.multiply(self.hr,1./self.Sps)))
        self.b_sampler_cc_0_0.set_Sps(self.Sps)
        self.b_Eye_Diagram_simple_c_0_0_1.set_Sps1(self.Sps)
        self.b_Eye_Diagram_simple_c_0_0_0.set_Sps1(self.Sps)
        self.b_Eye_Diagram_simple_c_0_0.set_Sps1(self.Sps)
        self.b_Eye_Diagram_simple_c_0.set_Sps1(self.Sps)
        self.set_Rs(self.samp_rate/self.Sps)

    def get_M(self):
        return self.M

    def set_M(self, M):
        self.M = M
        self.set_Bps(int(math.log(self.M,2)))

    def get_rolloff(self):
        return self.rolloff

    def set_rolloff(self, rolloff):
        self.rolloff = rolloff
        self.set_hrrc(wform.rrcos(self.Sps,self.ntaps,self.rolloff))
        self.set_hrc(wform.rcos(self.Sps,self.ntaps,self.rolloff))

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.set_hrrc(wform.rrcos(self.Sps,self.ntaps,self.rolloff))
        self.set_hrc(wform.rcos(self.Sps,self.ntaps,self.rolloff))
        self.set_hr(wform.rect(self.Sps,self.ntaps))
        self.set_hn(wform.nyq(self.Sps,self.ntaps))

    def get_Rs(self):
        return self.Rs

    def set_Rs(self, Rs):
        self.Rs = Rs
        self.set_Tmax_scope(64./self.Rs)
        self.set_Rb(self.Rs*self.Bps)

    def get_Bps(self):
        return self.Bps

    def set_Bps(self, Bps):
        self.Bps = Bps
        self.set_Rb(self.Rs*self.Bps)

    def get_run_stop(self):
        return self.run_stop

    def set_run_stop(self, run_stop):
        self.run_stop = run_stop
        self._run_stop_callback(self.run_stop)
        if self.run_stop: self.start()
        else: self.stop(); self.wait()

    def get_hrrc(self):
        return self.hrrc

    def set_hrrc(self, hrrc):
        self.hrrc = hrrc
        self.interp_fir_filter_xxx_0_0_1_0.set_taps((numpy.multiply(self.hrrc,1./self.Sps)))
        self.interp_fir_filter_xxx_0_0_0_0_1.set_taps((self.hrrc))

    def get_hrc(self):
        return self.hrc

    def set_hrc(self, hrc):
        self.hrc = hrc
        self.interp_fir_filter_xxx_0_0_2.set_taps((numpy.multiply(self.hrc,1./self.Sps)))
        self.interp_fir_filter_xxx_0_0_0_0_0.set_taps((self.hrc))

    def get_hr(self):
        return self.hr

    def set_hr(self, hr):
        self.hr = hr
        self.interp_fir_filter_xxx_0_0_0.set_taps((self.hr))
        self.interp_fir_filter_xxx_0_0.set_taps((numpy.multiply(self.hr,1./self.Sps)))

    def get_hn(self):
        return self.hn

    def set_hn(self, hn):
        self.hn = hn
        self.interp_fir_filter_xxx_0_0_1.set_taps((numpy.multiply(self.hn,1./self.Sps)))
        self.interp_fir_filter_xxx_0_0_0_0.set_taps((self.hn))

    def get_Tmax_scope(self):
        return self.Tmax_scope

    def set_Tmax_scope(self, Tmax_scope):
        self.Tmax_scope = Tmax_scope

    def get_TimingDelay(self):
        return self.TimingDelay

    def set_TimingDelay(self, TimingDelay):
        self.TimingDelay = TimingDelay
        self.b_sampler_cc_0_0.set_DelayDiez(self.TimingDelay)

    def get_Rb(self):
        return self.Rb

    def set_Rb(self, Rb):
        self.Rb = Rb

    def get_NodB(self):
        return self.NodB

    def set_NodB(self, NodB):
        self.NodB = NodB

    def get_MiconstellationObject(self):
        return self.MiconstellationObject

    def set_MiconstellationObject(self, MiconstellationObject):
        self.MiconstellationObject = MiconstellationObject

    def get_Fc(self):
        return self.Fc

    def set_Fc(self, Fc):
        self.Fc = Fc

    def get_BW(self):
        return self.BW

    def set_BW(self, BW):
        self.BW = BW


def main(top_block_cls=Lab_total, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
