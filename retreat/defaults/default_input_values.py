"""default_input_values"""
def my_defaults(cwd):
    """Dictionary containing Default Input Values"""
    from obspy.core import UTCDateTime
    # default parameter values:
    defaults = dict(
        #########################
        # DATA SOURCES - REALTIME
        myclient="IRIS",
        connection=['FDSN', 'seedlink'],
        # DATA SOURCES - REPLAY
        replay=False,
        customfmt=False,
        sds_root=cwd+"/retreat/example_data",
        sds_type=['', '*', 'D', 'R'],
        myFMTSTR="{year}/{network}/{station}/{channel}/"\
        "{network}.{station}.{location}.{channel}.{year}.{doy:03d}.00.00.mseed",
        dataformat=['MSEED', 'SAC', 'GCF', 'SEISAN'],
        # SCNL
        S="SP??",
        C="HHZ",
        N="NO",
        L="00",
        # METADATA
        inv_type=['STATIONXML', 'SEED', 'XSEED', 'RESP'],
        inv_supply=False,
        inv_file=cwd+"/retreat/example_data/dataless.seed.UR",
        # PRE-PROCESSING
        decimate=True,
        newfreq=20.0,
        demean=True,
        detrend=True,
        bandpass=True,
        Fmin=0.1,
        Fmax=10.0,
        prefilt=True,
        removeresponse=True,
        taper=True,
        taper_pc=0.005,
        zcomps=True,
        # TIMING
        plot_window=3600,
        window_length=120,
        update_interval=60,
        tstart=UTCDateTime().isoformat(),
        prebuf=30,
        fill_on_start=True,
        # ARRAY PROCESSING
        sll_x=-0.6,
        sll_y=-0.6,
        slm_x=0.6,
        slm_y=0.6,
        sl_s=0.025,
        win_len=10.0,
        win_frac=0.25,
        prewhiten=False,
        frqlow=0.5,
        frqhigh=5.0,
        semb_thresh='-1e9',
        vel_thresh='-1e9',
        nbin_baz=72, # 360/72=5 deg bins
        nbin_slow=50,
        # PLOTTING
        baz=True,
        slow=True,
        polar=True,
        rmes=True,
        rmes_wind=300.0,
        rmes_ovlp=0.90,
        seis=True,
        spec=True,
        resp=False,
        bazmap=True,
        elev_in_m=True,
        klim=30.0,
        kstep=0.025,
        timestamp=True,
        usestack=True,
        savefig=False,
        webfigs=False,
        logos=True,
        # PLOT DIMENSIONS
        timelinex=1600,
        timeliney=1200,
        polarx=800,
        polary=600,
        arrayx=650,
        arrayy=600,
        mapx=650,
        mapy=650,
        # AXIS LIMITS
        slow_ymin="auto",
        slow_ymax="auto",
        baz_ymin="auto",
        baz_ymax="auto",
        rms_ymin="auto",
        rms_ymax="auto",
        seis_ymin="auto",
        seis_ymax="auto",
        # SPECTROGRAM
        fmin=0.1,
        fmax=2.0,
        wlen=25.0,
        per_lap=0.95,
        clim1=0.75,
        clim2=1.0,
        cmap="jet",
        # MAP
        map_array_centre=True,
        map_array_radius=25, # km
        lon_min="auto",
        lon_max="auto",
        lat_min="auto",
        lat_max="auto",
        # OUTPUT
        #logpath=os.getcwd(),
        logpath=cwd+"/retreat/output/",
        logfile="retreat.log",
        #figpath=os.getcwd()+"/retreat/output/",
        figpath=cwd+"/retreat/output/",
        timelinefigname="MainTimeline",
        polarfigname="fkpolar",
        arrayfigname="arrayresp",
        mapfigname="map",
        ########################
    )
    return defaults
