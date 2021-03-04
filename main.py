import pandas as pd
import bar_chart_race as bcr
import ntpath

class BCR_Main:
        
    def __init__(self, file_path, image_path, save_location, title_name, 
                bar_size, color_palette, text_after_bar_label, bar_label_text_type, fps):
        
        self.path = file_path
        self.i_path = image_path
        self.location = save_location
        self.title_name = title_name
        self.bar_size = bar_size
        self.color_palette = color_palette
        self.text_after_bar_label = text_after_bar_label
        self.bar_label_text_type = bar_label_text_type
        self.fps = fps

        df = pd.read_csv(self.path, index_col='Date')

        # replace empty values with 0
        df.fillna(0.0, inplace=True)

        import matplotlib as mpl
        from matplotlib import font_manager as fm

        font_dirs = ['fonts/', ]
        font_files = fm.findSystemFonts(fontpaths=font_dirs)
        font_list = fm.createFontList(font_files)
        fm.fontManager.ttflist.extend(font_list)

        mpl.rcParams['font.family'] = 'Euclid Circular A'

        # get file name
        file_name = ntpath.basename(self.path).split('.')[0]

        # handle video name
        if self.title_name == '':
            self.title_name = file_name
        
        # handle none value of location
        if self.location == None:
            self.location = str(file_name) + ".mp4"
        else:
            self.location = self.location + "/" + str(file_name) + ".mp4"

        # handle the type of bar label text
        if self.bar_label_text_type == 'Decimal':
            bar_label_text = '{x:,.2f}'
        elif self.bar_label_text_type == 'Integer':
            bar_label_text = '{x:,.0f}'
        else:
            bar_label_text = '{x:,.0f}'

        # if image folder is not choen, reposition the bar label text (push towards the bar)
        if self.i_path == None:
            self.bar_label_position = 0.008
        else:
            self.bar_label_position = 0.05


        # plotting the graph
        bcr.bar_chart_race(
            df=df.head(5),
            filename=self.location,
            orientation='h',
            sort='desc',
            n_bars=10,
            fixed_order=False,
            fixed_max=False,
            steps_per_period=45, # smoothness
            period_length=1500,     # time period in ms per data
            fps=self.fps,
            interpolate_period=False,
            # label_bars=True,
            bar_size=self.bar_size,
            period_label={'x': .95, 'y': .15,
                        'ha': 'right',
                        'va': 'center',
                        'size': 72,
                        'weight': 'semibold'
                        },
            
            # period_summary_func=lambda v, r: {'x': .99, 'y': .1,
            #                                   's': "",
            #                                   'ha': 'right', 'size': 15, 'family': 'Courier New'},

            shared_fontdict={'family': 'Euclid Circular A',
                            'weight': 'medium', 'color': '#25265E'},

            perpendicular_bar_func=None,
            # figsize=(26.24, 15),    # resolution (4k -> (26.24,15))
            # dpi=144,
            # cmap='brand_colors',
            # title='Programming Language Popularity 1990 - 2020',
            # title_size=52,
            # bar_label_size=27,  # bar text size
            # tick_label_size=27, # y-axis text size
            scale='linear',
            writer=None,
            fig=None,
            bar_kwargs={'alpha': .99, 'lw': 0},
            filter_column_colors=True,

            # change
            fig_kwargs={'figsize':(26.67, 15), 'dpi':144, 'facecolor': '#F8FAFF'} ,
            # colors='brand_colors',
            colors=self.color_palette,
            title={'label': self.title_name,
                    'size': 52,
                    'weight': 'bold',
                    # 'loc': 'right',
                    'pad': 40},
            bar_label_font={'size':27},  # bar text size
            tick_label_font={'size':27}, # y-axis text size
            img_label_folder=self.i_path,

            bar_texttemplate=bar_label_text+str(self.text_after_bar_label),
            bar_label_position = self.bar_label_position,
        )