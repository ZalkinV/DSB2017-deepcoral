config = {'stage1_data_path':'/home/itip_m3406/Yukhtenko/brainTumorData',
          'luna_raw':'/data/torrent/rawdata/',
          'luna_segment':'/home/itip_m3406/Yukhtenko/seg-lungs-LUNA16/',
          
          'luna_data':'/home/itip_m3406/Yukhtenko/trainRes/lunaData/',
          'preprocess_result_path':'/home/itip_m3406/Yukhtenko/trainRes/preprocResPath/',       
          
          'luna_abbr':'./detector/labels/shorter.csv',
          'luna_label':'./detector/labels/lunaqualified.csv',
          'stage1_annos_path_old':['./detector/labels/label_job5.csv',
                './detector/labels/label_job4_2.csv',
                './detector/labels/label_job4_1.csv',
                './detector/labels/label_job0.csv',
                './detector/labels/label_qualified.csv'],
          'stage1_annos_path':['/home/itip_m3406/Yukhtenko/labels.csv'],
          'bbox_path':'../detector/results/res18/bbox/',
          'preprocessing_backend':'python'
         }
