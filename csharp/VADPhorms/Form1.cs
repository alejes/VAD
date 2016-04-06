using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using System.Windows.Forms.DataVisualization.Charting;
using NAudio.Wave;
using NAudio.FileFormats;
using NAudio.CoreAudioApi;
using NAudio;

namespace VADPhorms {
    public partial class Form1 : Form {
        // WaveIn - поток для записи
        WaveIn waveIn;
        //Класс для записи в файл
        WaveFileWriter writer;
        //Имя файла для записи
        string outputFilename = "out.wav";

        //Получение данных из входного буфера 
        /*
        void waveIn_DataAvailable(object sender, WaveInEventArgs e) {
            if (this.InvokeRequired) {
                this.BeginInvoke(new EventHandler<WaveInEventArgs>(waveIn_DataAvailable), sender, e);
            }
            else {
                //Записываем данные из буфера в файл
                writer.WriteData(e.Buffer, 0, e.BytesRecorded);
            }
        }
        */
        //получение данных из входного буфера для распознавания
        void waveIn_DataAvailable(object sender, WaveInEventArgs e) {
            if (this.InvokeRequired) {
                this.BeginInvoke(new EventHandler<WaveInEventArgs>(waveIn_DataAvailable), sender, e);
            }
            else {
                //переменная для обозначения начала распознавания речевого отрезка
                bool result = ProcessData(e);
                // Если записываемый отрезок содержит речь
                if (result == true) {
                    // обрабатываем звуковые данные
                    pictureBox1.Visible = true;
                    writer.WriteData(e.Buffer, 0, e.BytesRecorded);
                }
                else {
                    pictureBox1.Visible = false;
                    //MessageBox.Show("Речи небыло");
                    // если речь не определена на звуковом отрезке
                }
            }
        }

        private bool _isActive = false;
        //Завершаем запись
        void StopRecording() {
            //MessageBox.Show("StopRecording");
            if (_isActive) {
                _isActive = false;
                buttonStart.Enabled = true;
                buttonEnd.Enabled = false;
                waveIn.StopRecording();
            }
        }
        //Окончание записи
        private void waveIn_RecordingStopped(object sender, EventArgs e) {
            if (this.InvokeRequired) {
                this.BeginInvoke(new EventHandler(waveIn_RecordingStopped), sender, e);
            }
            else {
                waveIn.Dispose();
                waveIn = null;
                writer.Close();
                writer = null;
            }
        }

        private void ProcessWave(WaveInEventArgs e)
        {
            if (checkBoxWave.Checked)
            {
                errorLog.Text = e.BytesRecorded.ToString() + " " + e.GetHashCode();
                for (var index = 0; index < e.BytesRecorded; index += 2)
                {
                    double tmp = (short) ((e.Buffer[index + 1] << 8) | e.Buffer[index + 0]);
                    tmp /= 32768.0;
                    //if (tmp > )
                    //{

                    //}
                    chart1.Series["wave"].Points.Add(new DataPoint((_currentTime.AddMilliseconds(index*((double)MillisecOnEvent/e.BytesRecorded)) - _startingTime).TotalSeconds, tmp));
                    while (chart1.Series["wave"].Points.Count > 10000)
                    {
                        chart1.Series["wave"].Points.Remove(chart1.Series["wave"].Points.First());
                    }
                }
            }
            else
            {
                for (var index = 0; index < e.BytesRecorded; index += 2) {
                    if (chart1.Series["wave"].Points.Count <= 0) break;
                    chart1.Series["wave"].Points.Remove(chart1.Series["wave"].Points.First());
                }
            }
        }

        private void ProcessEnergy(WaveInEventArgs e)
        {
            if (checkBoxEnergy.Checked)
            {
                double sum = 0;
                for (var index = 0; index < e.BytesRecorded; index += 2)
                {
                    double tmp = (short)((e.Buffer[index + 1] << 8) | e.Buffer[index + 0]);
                    tmp /= 32768.0;
                    sum += tmp*tmp;

                }
                for (var index = 0; index < e.BytesRecorded; index += 2)
                {
                    chart1.Series["energy"].Points.Add(new DataPoint((_currentTime.AddMilliseconds(index * ((double)MillisecOnEvent / e.BytesRecorded)) - _startingTime).TotalSeconds, sum));
                    while (chart1.Series["energy"].Points.Count > 10000)
                    {
                        chart1.Series["energy"].Points.Remove(chart1.Series["energy"].Points.First());
                    }
                }
            }
            else
            {
                for (var index = 0; index < e.BytesRecorded; index += 2)
                {
                    if (chart1.Series["energy"].Points.Count <= 0) break;
                    chart1.Series["energy"].Points.Remove(chart1.Series["energy"].Points.First());
                }
            }
        }

        private void ProcessConstant(WaveInEventArgs e) {
            if (checkBoxConstant.Checked)
            {
                for (var index = 0; index < e.BytesRecorded; index += 2)
                {
                    //double tmp = (short)((e.Buffer[index + 1] << 8) | e.Buffer[index + 0]);
                    //tmp /= 32768.0;
                    chart1.Series["constant"].Points.Add(new DataPoint((_currentTime.AddMilliseconds(index * ((double)MillisecOnEvent / e.BytesRecorded)) - _startingTime).TotalSeconds, 700));
                    while (chart1.Series["constant"].Points.Count > 10000)
                    {
                        chart1.Series["constant"].Points.Remove(chart1.Series["constant"].Points.First());
                    }
                }
            }
            else
            {
                for (var index = 0; index < e.BytesRecorded; index += 2)
                {
                    if (chart1.Series["constant"].Points.Count <= 0) break;
                        chart1.Series["constant"].Points.Remove(chart1.Series["constant"].Points.First());
                }
            }

        }

        private static double porog = 0.02;
        // Обработчка речи - вычисляем, есть ли сама речь на звуковом отрезке
        private bool ProcessData(WaveInEventArgs e) {
            // Порог для вычисления наличия речи
            ProcessWave(e);
            ProcessConstant(e);
            ProcessEnergy(e);
            //startingTime += DateTime.Now;MillisecOnEvent;
            _currentTime = _currentTime.AddMilliseconds(MillisecOnEvent);
            chartArea.RecalculateAxesScale();
            bool result = false;
            bool Tr = false;
            double Sum2 = 0;
            int Count = e.BytesRecorded / 2;
            for (int index = 0; index < e.BytesRecorded; index += 2) {
                double Tmp = (short)((e.Buffer[index + 1] << 8) | e.Buffer[index + 0]);
                Tmp /= 32768.0;
                Sum2 += Tmp * Tmp;
                if (Tmp > porog)
                    Tr = true;
            }
            Sum2 /= Count;
            if (Tr || Sum2 > porog) { result = true; }
            else { result = false; }
            return result;
        }

        private ChartArea chartArea;
        public Form1() {
            InitializeComponent();

            chartArea = chart1.ChartAreas.FindByName("ChartArea1") ?? new ChartArea();
            chartArea.Name = "MyChartArea";
            chartArea.AxisX.Title = "Time";
            chartArea.AxisY.Title = "Value";
            //chartArea.AxisX.IntervalType = DateTimeIntervalType.Seconds;
            chartArea.AxisX2.Interval = 1;
            chartArea.AxisX2.IntervalType = DateTimeIntervalType.Seconds;
            chartArea.AxisX2.IntervalOffset = 1;
            chartArea.AxisX2.IntervalOffsetType = DateTimeIntervalType.Minutes;

            //chartArea.AxisY2.MaximumAutoSize = 2.0F;
            //chartArea.AxisX.Maximum = 1000;

            //Начало записи
            chart1.Series.Add("wave");
            chart1.Series["wave"].ChartType =
                System.Windows.Forms.DataVisualization.Charting.SeriesChartType.FastLine;
            //chart1.Series["wave"].ChartArea = "ChartArea1";
            chart1.Series.Add("constant");
            chart1.Series["constant"].ChartType =
                System.Windows.Forms.DataVisualization.Charting.SeriesChartType.FastLine;
            chart1.Series.Add("energy");
            chart1.Series["energy"].ChartType =
                System.Windows.Forms.DataVisualization.Charting.SeriesChartType.FastLine;
            //chart1.Series["constant"].ChartArea = "ChartArea1";
            //chart1.ChartAreas.Add(chartArea);
            //chart1.Series["constant"].Color = 

        }

        const int MillisecOnEvent = 50;
        private DateTime _startingTime;
        private DateTime _currentTime;
        private void button1_Click(object sender, EventArgs e) {
            try
            {
                if (_isActive) return;
                _isActive = true;
                buttonStart.Enabled = false;
                buttonEnd.Enabled = true;
                chart1.Series["wave"].Points.Clear();
                chart1.Series["constant"].Points.Clear();
                chart1.Series["energy"].Points.Clear();
                //MessageBox.Show("Start Recording");
                waveIn = new WaveIn();
                //Дефолтное устройство для записи (если оно имеется)
                //встроенный микрофон ноутбука имеет номер 0
                waveIn.DeviceNumber = 0;
                waveIn.BufferMilliseconds = MillisecOnEvent;
                //Прикрепляем к событию DataAvailable обработчик, возникающий при наличии записываемых данных
                waveIn.DataAvailable += waveIn_DataAvailable;
                //Прикрепляем обработчик завершения записи
                waveIn.RecordingStopped += new EventHandler<StoppedEventArgs>(waveIn_RecordingStopped);
                //Формат wav-файла - принимает параметры - частоту дискретизации и количество каналов(здесь mono)
                waveIn.WaveFormat = new WaveFormat(8000, 1);
                //Инициализируем объект WaveFileWriter
                writer = new WaveFileWriter(outputFilename, waveIn.WaveFormat);
                waveIn.StartRecording();
                _startingTime = DateTime.Now;
                _currentTime = DateTime.Now;
            }
            catch (Exception ex) {
                MessageBox.Show(ex.Message);
            }
        }

        private void button2_Click(object sender, EventArgs e) {
            if (waveIn != null) {
                StopRecording();
            }
        }

        private void pictureBox1_Click(object sender, EventArgs e) {

        }

        private void pictureBox1_Click_1(object sender, EventArgs e) {

        }

        private void checkBoxConstant_CheckedChanged(object sender, EventArgs e) {
            //if (!checkBoxConstant.Checked){   
                //chart1.Series["constant"].Points.Clear();
            //}
        }

        private void chart1_Click(object sender, EventArgs e)
        {

        }
    }
}






