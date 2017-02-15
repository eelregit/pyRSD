base_model_params = {'sigma8_z': 'mass variance at r = 8 Mpc/h at z',
                     'f': 'growth rate, f = dlnD/dlna at z', 
                     'alpha_perp': 'perpendicular Alcock-Paczynski effect parameter', 
                     'alpha_par': 'parallel Alcock-Paczynski effect parameter', 
                     'alpha_drag': 'ratio of sound horizon at z_drag in the fiducial and true cosmologies',
                     'b1_sA': 'linear bias of sats w/o other sats in same halo',
                     'b1_sB': 'linear bias of sats w/ other sats in same halo',
                     'b1_cA': 'linear bias of cens w/o sats in same halo',
                     'b1_cB': 'linear bias of cens w/ sats in same halo',
                     'fcB': 'fraction of cens with sats in same halo',
                     'fsB': 'fraction of sats with other sats in same halo', 
                     'fs': 'fraction of total galaxies that are satellites',
                     'NcBs': 'amplitude of 1-halo power for cenB-sat in (Mpc/h)^3', 
                     'NsBsB': 'amplitude of 1-halo power for satB-satB in (Mpc/h)^3', 
                     'sigma_c': 'centrals FOG damping in Mpc/h',
                     'sigma_s': 'satellite FOG damping in Mpc/h',
                     'sigma_sA': 'satA FOG damping in Mpc/h', 
                     'sigma_sB': 'satB FOG damping in Mpc/h',
                     'small_scale_sigma': 'additional small scale velocity in km/s',
                     'N' : 'constant offset to model, in (Mpc/h)^3', 
                     'f_so' : 'so vs fof fraction', 
                     'log10_fso' : 'log10 of so vs fof fraction',
                     'sigma_so' : 'so vs fof sigma',
                     'sigma_v' : 'the velocity dispersions',
                     'b2_00_a__0' : "A0 for b2_00_a",
                     'b2_00_a__2' : "A2 for b2_00_a",
                     'b2_00_a__4' : "A4 for b2_00_a",
                     'b2_00_b__0' : "A0 for b2_00_b",
                     'b2_00_b__2' : "A2 for b2_00_b",
                     'b2_00_b__4' : "A4 for b2_00_b",
                     'b2_00_c__0' : "A0 for b2_00_c",
                     'b2_00_c__2' : "A2 for b2_00_c",
                     'b2_00_c__4' : "A4 for b2_00_c",
                     'b2_00_d__0' : "A0 for b2_00_d",
                     'b2_00_d__2' : "A2 for b2_00_d",
                     'b2_00_d__4' : "A4 for b2_00_d",
                     'b2_01_a__0' : "A0 for b2_01_a",
                     'b2_01_a__1' : "A1 for b2_01_a",
                     'b2_01_a__2' : "A2 for b2_01_a",
                     'b2_01_b__0' : "A0 for b2_01_b",
                     'b2_01_b__1' : "A1 for b2_01_b",
                     'b2_01_b__2' : "A2 for b2_01_b",
                    }

extra_model_params = {'b1_s': 'linear bias of satellites',
                      'b1_c': 'linear bias of centrals', 
                      'b1': 'the total linear bias', 
                      'fsigma8' : 'f(z)*sigma8(z) at z of measurement',
                      'b1sigma8' : 'b1*sigma8(z) at z of measurement', 
                      'F_AP' : 'the AP parameter: alpha_par/alpha_perp',
                      'alpha' : 'the isotropic dilation',
                      'epsilon' : 'the anisotropic warping'
                      }
                    
from .power_gal import GalaxyPowerParameters, GalaxyPowerTheory