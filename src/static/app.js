var app = angular.module("geototypeApp", []);

app.factory('gm', function() {
    var gm = {
        geometries : {},
        createLine  : function(name, color, points, isClose) {
            var material = new THREE.LineBasicMaterial({
                color: color,
                linewidth : 3
            });
            var geometry = new THREE.BufferGeometry();
            var ps = points.length;
            if (isClose) {
                ps++;
            }
            var positions = new Float32Array(ps * 3);
            geometry.addAttribute( 'position', new THREE.BufferAttribute( positions, 3 ) );
            geometry.setDrawRange(0, ps);
            var idx = 0;
            for (var i=0; i<points.length; i++) {
                positions[idx++] = points[i][0];
                positions[idx++] = 0;
                positions[idx++] = points[i][1];
            }
            if (isClose) {
                positions[idx++] = points[0][0];
                positions[idx++] = 0;
                positions[idx++] = points[0][1];
            }

            var line = new THREE.Line(geometry, material);
            line.isClose = isClose;
            this.geometries[name] = line;
            return line;
        },
        updateLine     : function(name, color, points) {
            var line = this.geometries[name];
            var positions = line.geometry.attributes.position.array;

            var idx = 0;
            for (var i=0; i<points.length; i++) {
                positions[idx++] = points[i][0];
                positions[idx++] = 0;
                positions[idx++] = points[i][1];
            }
            if (line.isClose) {
                positions[idx++] = points[0][0];
                positions[idx++] = 0;
                positions[idx++] = points[0][1];
            }
            line.geometry.attributes.position.needsUpdate = true; // required after the first render
        },
        contain         : function(name) {
            return name in this.geometries;
        }
    };
    return gm;
});

app.factory('view', function(gm) {
    var view = {
        update  : function(data) {
            for (var name in data.E) {
                if (gm.contain(name) == false) {
                    this.scene.add(gm.createLine(name, 0x00ff00, data.E[name], true));
                } else {
                    gm.updateLine(name, 0x00ff00, data.E[name]);
                }
            }
        },
        render  : function() {
            this.renderer.render(this.scene, this.camera);
        }
    };
    var jnode = $('#renderPanel');
    var node = document.getElementById('renderPanel');
    var windowWidth     = jnode.parent().width();
    var windowHeight    = (windowWidth / 4) * 3;
    console.debug(windowWidth);
    console.debug(windowHeight);
    scene      = new THREE.Scene();
    camera     = new THREE.PerspectiveCamera( 70, windowWidth / windowHeight, 1, 1000 );
    renderer   = new THREE.WebGLRenderer();
    light      = new THREE.DirectionalLight( 0xffffff );
    camera.position.y=80;
    camera.position.x=50;
    camera.position.z=50;
    camera.lookAt({x:50, y:0, z:50});
    renderer.setSize( windowWidth, windowHeight );
    node.appendChild( renderer.domElement );

    var LineMaterial  = new THREE.LineBasicMaterial({
        color: 0x0000ff
    });

    for (i=0; i<=100; i+=10)
    {
        {
            var geometry = new THREE.Geometry();
            geometry.vertices.push( new THREE.Vector3( i, 0, 0) );
            geometry.vertices.push( new THREE.Vector3( i, 0, 100 ) );

            var line = new THREE.Line( geometry, LineMaterial );
            scene.add( line );
        }
        {
            var geometry = new THREE.Geometry();
            geometry.vertices.push( new THREE.Vector3( 0, 0, i) );
            geometry.vertices.push( new THREE.Vector3( 100, 0, i ) );

            var line = new THREE.Line( geometry, LineMaterial );
            scene.add( line );
        }
    }
    light.position.set( 0, 1, 0 );
    scene.add(light);

    view.scene      = scene;
    view.camera     = camera;
    view.renderer   = renderer;
    view.light      = light;

    return view;
});
