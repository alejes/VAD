namespace VADPhorms {
    partial class Form1 {
        /// <summary>
        /// Требуется переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing) {
            if (disposing && (components != null)) {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Обязательный метод для поддержки конструктора - не изменяйте
        /// содержимое данного метода при помощи редактора кода.
        /// </summary>
        private void InitializeComponent() {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea3 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            this.buttonStart = new System.Windows.Forms.Button();
            this.buttonEnd = new System.Windows.Forms.Button();
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.checkBoxWave = new System.Windows.Forms.CheckBox();
            this.chart1 = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.checkBoxConstant = new System.Windows.Forms.CheckBox();
            this.errorLog = new System.Windows.Forms.Label();
            this.checkBoxEnergy = new System.Windows.Forms.CheckBox();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.chart1)).BeginInit();
            this.SuspendLayout();
            // 
            // buttonStart
            // 
            this.buttonStart.Location = new System.Drawing.Point(24, 318);
            this.buttonStart.Name = "buttonStart";
            this.buttonStart.Size = new System.Drawing.Size(75, 23);
            this.buttonStart.TabIndex = 0;
            this.buttonStart.Text = "Start";
            this.buttonStart.UseVisualStyleBackColor = true;
            this.buttonStart.Click += new System.EventHandler(this.button1_Click);
            // 
            // buttonEnd
            // 
            this.buttonEnd.Enabled = false;
            this.buttonEnd.Location = new System.Drawing.Point(160, 318);
            this.buttonEnd.Name = "buttonEnd";
            this.buttonEnd.Size = new System.Drawing.Size(75, 23);
            this.buttonEnd.TabIndex = 1;
            this.buttonEnd.Text = "Stop";
            this.buttonEnd.UseVisualStyleBackColor = true;
            this.buttonEnd.Click += new System.EventHandler(this.button2_Click);
            // 
            // pictureBox1
            // 
            this.pictureBox1.Image = ((System.Drawing.Image)(resources.GetObject("pictureBox1.Image")));
            this.pictureBox1.InitialImage = ((System.Drawing.Image)(resources.GetObject("pictureBox1.InitialImage")));
            this.pictureBox1.Location = new System.Drawing.Point(-1, 1);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(56, 55);
            this.pictureBox1.TabIndex = 2;
            this.pictureBox1.TabStop = false;
            this.pictureBox1.Visible = false;
            this.pictureBox1.Click += new System.EventHandler(this.pictureBox1_Click_1);
            // 
            // checkBoxWave
            // 
            this.checkBoxWave.AutoSize = true;
            this.checkBoxWave.Checked = true;
            this.checkBoxWave.CheckState = System.Windows.Forms.CheckState.Checked;
            this.checkBoxWave.Location = new System.Drawing.Point(24, 358);
            this.checkBoxWave.Name = "checkBoxWave";
            this.checkBoxWave.Size = new System.Drawing.Size(55, 17);
            this.checkBoxWave.TabIndex = 3;
            this.checkBoxWave.Text = "Wave";
            this.checkBoxWave.UseVisualStyleBackColor = true;
            // 
            // chart1
            // 
            chartArea3.Name = "ChartArea1";
            this.chart1.ChartAreas.Add(chartArea3);
            this.chart1.Location = new System.Drawing.Point(-1, 61);
            this.chart1.Name = "chart1";
            this.chart1.Size = new System.Drawing.Size(714, 251);
            this.chart1.TabIndex = 4;
            this.chart1.Text = "chart1";
            this.chart1.Click += new System.EventHandler(this.chart1_Click);
            // 
            // checkBoxConstant
            // 
            this.checkBoxConstant.AutoSize = true;
            this.checkBoxConstant.Location = new System.Drawing.Point(86, 358);
            this.checkBoxConstant.Name = "checkBoxConstant";
            this.checkBoxConstant.Size = new System.Drawing.Size(68, 17);
            this.checkBoxConstant.TabIndex = 5;
            this.checkBoxConstant.Text = "Constant";
            this.checkBoxConstant.UseVisualStyleBackColor = true;
            this.checkBoxConstant.CheckedChanged += new System.EventHandler(this.checkBoxConstant_CheckedChanged);
            // 
            // errorLog
            // 
            this.errorLog.AutoSize = true;
            this.errorLog.Location = new System.Drawing.Point(590, 358);
            this.errorLog.Name = "errorLog";
            this.errorLog.Size = new System.Drawing.Size(35, 13);
            this.errorLog.TabIndex = 6;
            this.errorLog.Text = "label1";
            // 
            // checkBoxEnergy
            // 
            this.checkBoxEnergy.AutoSize = true;
            this.checkBoxEnergy.Location = new System.Drawing.Point(161, 358);
            this.checkBoxEnergy.Name = "checkBoxEnergy";
            this.checkBoxEnergy.Size = new System.Drawing.Size(59, 17);
            this.checkBoxEnergy.TabIndex = 7;
            this.checkBoxEnergy.Text = "Energy";
            this.checkBoxEnergy.UseVisualStyleBackColor = true;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(716, 380);
            this.Controls.Add(this.checkBoxEnergy);
            this.Controls.Add(this.errorLog);
            this.Controls.Add(this.checkBoxConstant);
            this.Controls.Add(this.chart1);
            this.Controls.Add(this.checkBoxWave);
            this.Controls.Add(this.pictureBox1);
            this.Controls.Add(this.buttonEnd);
            this.Controls.Add(this.buttonStart);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.chart1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button buttonStart;
        private System.Windows.Forms.Button buttonEnd;
        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.CheckBox checkBoxWave;
        private System.Windows.Forms.DataVisualization.Charting.Chart chart1;
        private System.Windows.Forms.CheckBox checkBoxConstant;
        private System.Windows.Forms.Label errorLog;
        private System.Windows.Forms.CheckBox checkBoxEnergy;
    }
}

