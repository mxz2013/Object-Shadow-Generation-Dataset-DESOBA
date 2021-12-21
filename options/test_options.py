from .base_options import BaseOptions


# class TestOptions(BaseOptions):
#     def initialize(self, parser):
#         parser = BaseOptions.initialize(self, parser)
#         parser.add_argument('--ntest', type=int, default=float("inf"), help='# of test examples.')
#         parser.add_argument('--results_dir', type=str, default='./results/', help='saves results here.')
#         parser.add_argument('--aspect_ratio', type=float, default=1.0, help='aspect ratio of result images')
#         parser.add_argument('--phase', type=str, default='test', help='train, val, test, etc')
#         #  Dropout and Batchnorm has different behavioir during training and test.
#         parser.add_argument('--eval', action='store_true', help='use eval mode during test time.')
#         parser.add_argument('--num_test', type=int, default=50, help='how many test images to run')

#         parser.add_argument('--niter', type=int, default=100, help='# of iter at starting learning rate')
#         parser.add_argument('--niter_decay', type=int, default=100, help='# of iter to linearly decay learning rate to zero')
#         parser.add_argument('--beta1', type=float, default=0.5, help='momentum term of adam')
#         parser.add_argument('--lr', type=float, default=0.0002, help='initial learning rate for adam')
#         parser.add_argument('--save_epoch_freq', type=int, default=5, help='frequency of saving checkpoints at the end of epochs')

#         parser.add_argument('--display_id', type=int, default=1, help='window id of the web display')
#         # parser.add_argument('--display_server', type=str, default="http://bigiris.cs.stonybrook.edu", help='visdom server of the web display')
#         parser.add_argument('--display_server', type=str, default="https://www.sjtu.edu.cn/", help='visdom server of the web display')

#         parser.add_argument('--display_env', type=str, default='main', help='visdom display environment name (default is "main")')
#         parser.add_argument('--param_path', type=str)
#         parser.add_argument('--display_port', type=int, default=8097, help='visdom port of the web display')
#         parser.add_argument('--update_html_freq', type=int, default=10000, help='frequency of saving training results to html')


#         parser.set_defaults(model='test')
#         # To avoid cropping, the loadSize should be the same as fineSize
#         parser.set_defaults(loadSize=parser.get_default('fineSize'))
#         self.isTrain = False
#         return parser


class TestOptions(BaseOptions):
    def initialize(self, parser):
        parser = BaseOptions.initialize(self, parser)
        parser.add_argument('--display_freq', type=int, default=40,
                            help='frequency of showing training results on screen')
        parser.add_argument('--display_ncols', type=int, default=4,
                            help='if positive, display all images in a single visdom web panel with certain number of images per row.')
        parser.add_argument('--display_id', type=int, default=-1, help='window id of the web display')
        # parser.add_argument('--display_server', type=str, default="http://bigiris.cs.stonybrook.edu", help='visdom server of the web display')
        parser.add_argument('--display_server', type=str, default="http://localhost:8097",
                            help='visdom server of the web display')

        parser.add_argument('--display_env', type=str, default='main',
                            help='visdom display environment name (default is "main")')
        parser.add_argument('--display_port', type=int, default=8097, help='visdom port of the web display')
        parser.add_argument('--update_html_freq', type=int, default=10000,
                            help='frequency of saving training results to html')
        parser.add_argument('--print_freq', type=int, default=100,
                            help='frequency of showing training results on console')
        parser.add_argument('--save_latest_freq', type=int, default=5000, help='frequency of saving the latest results')
        parser.add_argument('--save_epoch_freq', type=int, default=5,
                            help='frequency of saving checkpoints at the end of epochs')
        parser.add_argument('--continue_train', action='store_true', help='continue training: load the latest model')
        parser.add_argument('--epoch_count', type=int, default=1,
                            help='the starting epoch count, we save the model by <epoch_count>, <epoch_count>+<save_latest_freq>, ...')
        parser.add_argument('--phase', type=str, default='test', help='train, val, test, etc')
        parser.add_argument('--niter', type=int, default=100, help='# of iter at starting learning rate')
        parser.add_argument('--niter_decay', type=int, default=100,
                            help='# of iter to linearly decay learning rate to zero')
        parser.add_argument('--beta1', type=float, default=0.5, help='momentum term of adam')
        parser.add_argument('--lr', type=float, default=0.0002, help='initial learning rate for adam')
        parser.add_argument('--no_lsgan', action='store_true',
                            help='do *not* use least square GAN, if false, use vanilla GAN')
        parser.add_argument('--pool_size', type=int, default=50,
                            help='the size of image buffer that stores previously generated images')
        parser.add_argument('--no_html', action='store_true',
                            help='do not save intermediate training results to [opt.checkpoints_dir]/[opt.name]/web/')
        parser.add_argument('--lr_policy', type=str, default='lambda',
                            help='learning rate policy: lambda|step|plateau|cosine')
        parser.add_argument('--lr_decay_iters', type=int, default=50,
                            help='multiply by a gamma every lr_decay_iters iterations')

        parser.add_argument('--eval', action='store_true', help='use eval mode during test time.')

        parser.add_argument('--param_path', type=str)
        parser.add_argument('--light_path', type=str)
        parser.add_argument('--instance_path', type=str)
        parser.add_argument('--shadowimg_path', type=str)
        parser.add_argument('--shadowmask_path', type=str)
        parser.add_argument('--shadowfree_path', type=str)
        parser.add_argument('--light_vis_path', type=str)
        parser.add_argument('--bg_instance_path', type=str)
        parser.add_argument('--bg_shadow_path', type=str)
        parser.add_argument('--new_mask_path', type=str)


        parser.add_argument('--dataroot1',
                            help='path to images (should have subfolders trainA, trainB, valA, valB, etc)')
        parser.add_argument('--param_path1', type=str)
        parser.add_argument('--light_path1', type=str)
        parser.add_argument('--instance_path1', type=str)
        parser.add_argument('--shadowimg_path1', type=str)
        parser.add_argument('--shadowmask_path1', type=str)
        parser.add_argument('--shadowfree_path1', type=str)
        parser.add_argument('--light_vis_path1', type=str)
        parser.add_argument('--bg_instance_path1', type=str)
        parser.add_argument('--bg_shadow_path1', type=str)
        parser.add_argument('--redark_path1', type=str)
        parser.add_argument('--new_mask_path1', type=str)


        parser.add_argument('--lambda_P1', type=float, default=1)
        parser.add_argument('--lambda_M1', type=float, default=1)
        parser.add_argument('--lambda_I1', type=float, default=1)
        parser.add_argument('--lambda_STN1', type=float, default=1)
        parser.add_argument('--lambda_REF1', type=float, default=1)
        parser.add_argument('--lambda_TV1', type=float, default=1)

        ####stn network
        ####
        parser.add_argument('--stn_model_type', type=str, default='bounded_stn',
                            help='no_stn, unbounded_stn, bounded_stn')
        parser.add_argument('--grid_size', type=int, default=4)
        parser.add_argument('--angle', type=int, default=60)
        parser.add_argument('--span_range', type=int, default=0.9)
        parser.add_argument('--bg_selfattention', type=int, default=0)
        parser.add_argument('--bg_maskattention', type=int, default=0)
        parser.add_argument('--adain_mask_generator', type=int, default=0)

        parser.add_argument('--warp_N', type=int, default=1)

        # parser.add_argument('--resize_or_crop', type=str, default='resize_and_crop', help='scaling and cropping of images at load time [resize_and_crop|crop|scale_width|scale_width_and_crop|none]')

        self.isTrain = False
        return parser
