import sys
import nibabel as nib
import matplotlib.pyplot as plt

# -*-coding:utf-8-*-

def plot_slice(nii_file,out_pic):
    # read nii
    infile = nib.load(nii_file)
    info = infile.get_fdata()

    ## plotting
    row_num=6
    col_num=6
    total_num=row_num*col_num
    slice_num = info.shape[2]  #adjust scanning axis
    step  = slice_num // total_num
    real_range = total_num * step
    real_start = int((slice_num - real_range) / 2)

    fig, axs = plt.subplots(row_num, col_num, figsize=[15, 15])
    n=0
    for i in range(real_start,real_range,step):
        axs.flat[n].imshow(info[:,:,i], cmap='bone')
        n+=1

    plt.tight_layout()
    plt.savefig(out_pic)


if __name__=='__main__':
    nii_file=sys.argv[1] # './monkey.nii'
    out_pic=sys.argv[2] # './brain.png'
    plot_slice(nii_file,out_pic)