"""default_input_values"""
def my_defaults(cwd):
    """Dictionary containing Default Input Values"""
    from obspy.core import UTCDateTime
    # default parameter values:
    defaults = dict(
        #########################
        # DATA SOURCES - REALTIME
        myclient="IRIS",
        connection=['FDSN', 'seedlink','earthworm'],
        # DATA SOURCES - REPLAY
        replay=True,
        customfmt=True,
        sds_root=cwd+"/retreat/example_data",
        sds_type=['', '*', 'D', 'R'],
        myFMTSTR="{network}.{station}.{location}.{channel}.{year}.{doy:03d}.00.00.mseed",
        dataformat=['MSEED', 'SAC', 'GCF', 'SEISAN'],
        # SCNL
        S="UR*",
        C="HHZ",
        N="VI",
        L="",
        scnl_supply=False,
        scnl_file=cwd+"/retreat/example_data/UR.scnl",
        # METADATA
        inv_type=['SEED','STATIONXML', 'XSEED', 'RESP'],
        inv_supply=True,
        inv_file=cwd+"/retreat/example_data/dataless.seed.UR",
        # PRE-PROCESSING
        check_gaps=True,
        min_nchan=3,
        max_gap_size=10,
        max_gap_ends=60,
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
        window_length=600,
        update_interval=30,
        max_realtime_latency=180,
        tstart=UTCDateTime('2014-09-03-06:00').isoformat(),
        tstop=UTCDateTime('2014-09-03-08:01').isoformat(),
        prebuf=30,
        fill_on_start=True,
        # ARRAY PROCESSING
        sll_x=-0.6,
        sll_y=-0.6,
        slm_x=0.6,
        slm_y=0.6,
        sl_s=0.025,
        win_len=5.88,
        win_frac=0.30,
        prewhiten=False,
        frqlow=0.8,
        frqhigh=2.6,
        semb_thresh='-1e9',
        vel_thresh='-1e9',
        nbin_baz=72, # 360/72=5 deg bins
        nbin_slow=50,
        lsq=False,
        # PLOTTING
        baz=True,
        slow=True,
        polar=True,
        rmes=True,
        relpow=False,
        norm=False,
        rmes_wind=30.0,
        rmes_ovlp=0.90,
        seis=True,
        spec=True,
        resp=False,
        bazmap=True,
        elev_in_m=True,
        klim=10.0,
        kstep=0.01,
        timestamp=False,
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
        relpow_ymin="auto",
        relpow_ymax="auto",
        # SPECTROGRAM
        fmin=0.5,
        fmax=2.5,
        wlen=20.0,
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
        savedata=False,
        datafile="array_output",
        ########################
    )
    return defaults
