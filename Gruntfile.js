/*global module:false*/
module.exports = function(grunt) {

    // Project configuration.
    grunt.initConfig({
        uglify: {
            core: {
                files: [{
                    dest: 'static/js/core.min.js',
                    src: [
                        'bower_components/angular/angular.min.js',
                        'bower_components/angular-route/angular-route.min.js',
                        'bower_components/jquery/dist/jquery.min.js',
                        'bower_components/angular-ui/build/angular-ui.min.js',
                        'bower_components/angular-bootstrap/ui-bootstrap.min.js',
                        'bower_components/angular-bootstrap/ui-bootstrap-tpls.min.js',
                        'bower_components/satellizer/satellizer.min.js'
                    ],
                    nonull: true
                }]
            }
        },
        sass: {
            dist: {
                files: [{
                    expand: true,
                    cwd: 'static/sass',
                    src: ['*.scss'],
                    dest: 'static/css',
                    ext: '.css'
                }]
            }
        },
        cssmin: {
            core: {
                files: [
                    {
                        dest: 'static/css/core.min.css',
                        src: [
                            'bower_components/bootstrap/dist/css/bootstrap.min.css',
                            'bower_components/angular-ui/build/angular-ui.min.css'
                        ],
                        nonull: true
                    },
                    {
                        dest: 'static/css/main.min.css',
                        src: [
                            'static/css/main.css'
                        ],
                        nonull: true
                    }]
            }
        },
        copy: {
            core: {
                files: [{
                    dest: 'static/fonts/',
                    src: [
                        'bower_components/font-awesome/fonts/*'
                    ],
                    nonull: true,
                    flatten: true,
                    expand: true
                }]
            }
        }
    });

    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-contrib-sass');

    // Default task.
    grunt.registerTask('default', ['uglify', 'sass', 'cssmin', 'copy']);

};
