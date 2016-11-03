app.controller('msgCtrl', function($scope, view) {
    $scope.wsOpen = function(event) {
        console.debug(event);
    };

    $scope.wsMessage = function(event) {
        message = JSON.parse(event.data);
        if (message.act === 1) { // JOIN SUCCESSFULLYj
            $scope.join_as_watcher();
        } else if (message.act === 7) {// PAINT PLEASE
            $scope.view.update(message);
        }
    };
    $scope.render = function() {
        loop=window.requestAnimationFrame( $scope.render);
        $scope.view.render();
    };

    $scope.join_as_watcher = function(name) {
        $scope.ws.send(JSON.stringify({
            act         : 2,
            room_id     : $scope.roomId,
            nick_id     : $scope.name,
            user_type   : 1
        }));
    };

    $scope.init = function (wsAddr, roomId, name) {
        $scope.name     = name;
        $scope.roomId   = roomId;
        $scope.view     = view;
        $scope.ws       = new WebSocket(wsAddr);
        $scope.ws.onopen    = $scope.wsOpen;
        $scope.ws.onmessage = $scope.wsMessage;
        $scope.render();
    };
});